
import numpy as np
import matplotlib.pyplot as plt


class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''

    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None

    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''

        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''

        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''

        rad = deg * (np.pi / 180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]])

    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''

        x_dim, y_dim = 1.2 * x_dim, 1.2 * y_dim
        plt.plot((-x_dim, x_dim), [0, 0], 'k-')
        plt.plot([0, 0], (-y_dim, y_dim), 'k-')
        plt.xlim(-x_dim, x_dim)
        plt.ylim(-y_dim, y_dim)
        plt.grid()
        plt.show()


class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''

    def __init__(self, A):
        '''
        Initializations here
        '''

        super().__init__()
        self.vertices = np.array(A)
        self.prevVertices = None  # keep hold of previous figure coordinates

    def translate(self, dx, dy):
        '''
        Function to translate the polygon

        This function takes 2 arguments: dx and dy

        This function returns the final coordinates
        '''

        self.prevVertices = np.array(self.vertices)  # updating previous figure coordinate

        new_x = []  # new x coordinates
        new_y = []  # new y coordinates

        super().translate(dx, dy)  # calling parent function

        # finding new coordinates after translation
        for i in range(len(self.vertices)):
            new_vertex = np.dot(self.T_t, self.vertices[i])
            self.vertices[i][0] = new_vertex[0]
            self.vertices[i][1] = new_vertex[1]
            new_x.append(round(new_vertex[0], 2))
            new_y.append(round(new_vertex[1], 2))

        return np.array(new_x), np.array(new_y)

    def scale(self, sx, sy):
        '''
        Function to scale the polygon

        This function takes 2 arguments: sx and sy

        This function returns the final coordinates
        '''
        temp = np.array(self.vertices)  # temporarily stoning current vertices for future use

        super().scale(sx, sy)  # calling parent function

        unscaled_mid_x = 0
        unscaled_mid_y = 0

        # finding centre of unscaled figure
        for i in range(len(self.vertices)):
            unscaled_mid_x += self.vertices[i][0]
            unscaled_mid_y += self.vertices[i][1]
        unscaled_mid_x /= len(self.vertices)
        unscaled_mid_y /= len(self.vertices)

        scaled_mid_x = 0
        scaled_mid_y = 0

        # scaling the figure and finding centre of scaled figure
        for i in range(len(self.vertices)):
            scaled_vertex = np.dot(self.T_s, self.vertices[i])
            self.vertices[i][0] = scaled_vertex[0]
            self.vertices[i][1] = scaled_vertex[1]
            scaled_mid_x += scaled_vertex[0]
            scaled_mid_y += scaled_vertex[1]

        scaled_mid_x /= len(self.vertices)
        scaled_mid_y /= len(self.vertices)

        # now we need to translate back our scaled figure so that previous unscaled and current scaled
        # figure's centre matches.
        place_back_centre = self.translate(unscaled_mid_x - scaled_mid_x, unscaled_mid_y - scaled_mid_y)
        self.prevVertices = temp  # updating previous figure coordinate using temporary variable
        return place_back_centre

    def rotate(self, deg, rx=0.0, ry=0.0):
        '''
        Function to rotate the polygon

        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)

        This function returns the final coordinates
        '''

        self.prevVertices = np.array(self.vertices)  # updating previous figure coordinate

        new_x = []
        new_y = []

        super().rotate(deg)  # calling parent function

        # rotating our figure
        for i in range(len(self.vertices)):
            x = self.vertices[i][0] - rx
            y = self.vertices[i][1] - ry
            result = np.dot(self.T_r, [[x], [y], [0]])
            tx = result[0][0] + rx
            ty = result[1][0] + ry
            self.vertices[i][0] = tx
            self.vertices[i][1] = ty
            new_x.append(round(tx, 2))
            new_y.append(round(ty, 2))

        return np.array(new_x), np.array(new_y)

    def plotHelper(self, vertices):
        """
        As we need to plot both previous fiure and current figure, both have some common work to do
        """

        pol = []
        axis_lim = 0
        for points in vertices:
            pol.append([points[0], points[1]])
            axis_lim = max(axis_lim, abs(points[0]), abs(points[1]))
        return (pol, axis_lim)

    def plot(self):
        '''
        Function to plot the polygon

        This function should plot both the initial and the transformed polygon

        This function should use the parent's class plot method as well

        This function does not take any input

        This function does not return anything
        '''
        if self.prevVertices is not None:  # if previous vertices is not None
            prev = self.plotHelper(self.prevVertices)
        curr = self.plotHelper(self.vertices)
        if self.prevVertices is not None:
            prev_pol = prev[0]
        curr_pol = curr[0]  # coordinates that will be plotted
        axis_lim = curr[1]  # axis limit is the maximum x or y coordinate out of previous and current figure
        if self.prevVertices is not None:
            axis_lim = max(prev[1], curr[1])
        if self.prevVertices is not None:
            prevPlot = plt.Polygon(prev_pol, fill=None, color="BLACK", linestyle="--")
        currPlot = plt.Polygon(curr_pol, fill=None, color="RED")
        if self.prevVertices is not None:
            plt.gca().add_patch(prevPlot)
        plt.gca().add_patch(currPlot)  # getting current axis and adding figure to it
        super().plot(axis_lim, axis_lim)  # calling parent function

    def __str__(self):
        """
         This will be used when we print an object of current class
        """
        string = ""
        for ele in self.vertices:
            string += "%s " % (round(ele[0], 2))
        for ele in self.vertices:
            string += "%s " % (round(ele[1], 2))
        print(string)
        return ""


class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''

    def __init__(self, x=0.0, y=0.0, radius=5.0):
        '''
        Initializations here
        '''

        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.prev_x = None
        self.prev_y = None
        self.prev_radius = None

    def translate(self, dx, dy):
        '''
        Function to translate the circle

        This function takes 2 arguments: dx and dy (dy is optional).

        This function returns the final coordinates and the radius
        '''

        # updating previous coordinates and radius
        self.prev_x = self.x
        self.prev_y = self.y
        self.prev_radius = self.radius

        super().translate(dx, dy)  # calling parent function

        result = np.dot(self.T_t, [self.x, self.y, 1])
        self.x = result[0]  # new x coordinate of centre after translation
        self.y = result[1]  # new y coordinate of centre after translation

        return round(self.x, 2), round(self.y, 2), round(self.radius, 2)

    def scale(self, sr):
        '''
        Function to scale the circle

        This function takes 1 argument: sr

        This function returns the final coordinates and the radius
        '''
        # updating previous coordinates and radius
        self.prev_x = self.x
        self.prev_y = self.y
        self.prev_radius = self.radius

        super().scale(sr, sr)  # calling parent function

        result = np.dot(self.T_s, [self.radius, 0, 0])
        self.radius = result[0]  # new scaled radius

        return round(self.x, 2), round(self.y, 2), round(self.radius, 2)

    def rotate(self, deg, rx=0.0, ry=0.0):
        '''
        Function to rotate the circle

        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)

        This function returns the final coordinates and the radius
        '''
        # updating previous coordinates and radius
        self.prev_x = self.x
        self.prev_y = self.y
        self.prev_radius = self.radius

        super().rotate(deg)  # calling parent function

        # rotating our figure
        x = self.x - rx
        y = self.y - ry
        result = np.dot(self.T_r, [[x], [y], [0]])
        tx = result[0][0] + rx
        ty = result[1][0] + ry
        self.x = tx
        self.y = ty

        return round(self.x, 2), round(self.y, 2), round(self.radius, 2)

    def plot(self):
        '''
        Function to plot the circle

        This function should plot both the initial and the transformed circle

        This function should use the parent's class plot method as well

        This function does not take any input

        This function does not return anything
        '''
        if self.prev_x is not None:
            prevCircle = plt.Circle((self.prev_x, self.prev_y), self.prev_radius, color="BLACK", fill=None,
                                    linestyle="--")
        currCircle = plt.Circle((self.x, self.y), self.radius, color="RED", fill=None)
        # axis limit is the maximum x or y coordinate possible out of previous and current figure
        axis_lim = max(abs(self.x), abs(self.y)) + self.radius
        if self.prev_x is not None:
            axis_lim = max(axis_lim, max(abs(self.prev_x), abs(self.prev_y)) + self.prev_radius)
        if self.prev_x is not None:
            plt.gca().add_patch(prevCircle)
        # getting the current axis and adding figure to it.
        plt.gca().add_patch(currCircle)
        super().plot(axis_lim, axis_lim)

    def __str__(self):
        """
        This will be used when we print an object of current class
        """
        print(round(self.x, 2), round(self.y, 2), round(self.radius, 2))
        return ""


if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''

    isPlot = False
    val = int(input("Verbose? 1 to plot, 0 otherwise: "))
    if val == 1:
        isPlot = True
    t = int(input("Enter number of test cases: "))
    while t > 0:
        shape = int(input("Enter type of shape(1 for circle, 0 for polygon): "))
        if shape == 1:
            str = input("Enter center coordinates and radus:").split(" ")
            c = Circle(float(str[0]), float(str[1]), float(str[2]))
            q = int(input("Enter number of queries: "))
            while q > 0:
                print("1) R deg (rx) (ry)")
                print("2) S sr")
                print("3) T dx (dy)")
                if isPlot:
                    print("4) P")
                str = input().split(" ")
                if str[0] == "R":
                    deg = float(str[1])
                    rx = 0
                    if len(str) > 2:
                        rx = float(str[2])
                    ry = 0
                    if len(str) > 3:
                        ry = float(str[3])
                    print(c)
                    c.rotate(deg, rx, ry)
                    print(c)
                elif str[0] == 'S':
                    sr = float(str[1])
                    print(c)
                    c.scale(sr)
                    print(c)
                elif str[0] == "T":
                    dx = float(str[1])
                    dy = dx
                    if len(str) > 2:
                        dy = float(str[2])
                    print(c)
                    c.translate(dx, dy)
                    print(c)
                elif isPlot and str[0] == "P":
                    c.plot()
                q -= 1
        else:
            sides = int(input("Enter number of sides: "))
            A = []
            for i in range(1, sides + 1):
                point = input("Enter (x%s, y%s): " % (i, i)).split(" ")
                A.append([float(point[0]), float(point[1]), 1])
            p = Polygon(A)
            q = int(input("Enter number of queries: "))
            while q > 0:
                print("1) R deg (rx) (ry)")
                print("2) S sx (sy)")
                print("3) T dx (dy)")
                if isPlot:
                    print("4) P")
                str = input().split(" ")
                if str[0] == "R":
                    deg = float(str[1])
                    rx = 0
                    if len(str) > 2:
                        rx = float(str[2])
                    ry = 0
                    if len(str) > 3:
                        ry = float(str[3])
                    print(p)
                    p.rotate(deg, rx, ry)
                    print(p)
                elif str[0] == 'S':
                    sx = float(str[1])
                    sy = sx
                    if len(str) > 2:
                        sy = float(str[2])
                    print(p)
                    p.scale(sx, sy)
                    print(p)
                elif str[0] == "T":
                    dx = float(str[1])
                    dy = dx
                    if len(str) > 2:
                        dy = float(str[2])
                    print(p)
                    p.translate(dx, dy)
                    print(p)
                elif isPlot and str[0] == 'P':
                    p.plot()
                q -= 1
        t -= 1
