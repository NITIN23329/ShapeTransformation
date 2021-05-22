## ShapeTransformation

# This project facilitates transformation on a variety of closed shapes like circles, squares, pentagons, or any closed polygon. We can plot these shapes and can view the changes that are made after the transformation. For transformation, I used 'numpy' module and for plotting figures, I used 'matplotlib'.

The transformation that can be done are:
  1) We scale shapes by a given factor in both x and y directions. 
  2) We can translate shapes along the x and y direction by a given amount.
  3) And even we can rotate them by a given angle and along a given axis of rotation.
  4) We can also see the coordinate of vertices in case of polygons and radius and centre in case of circle after the transformation.

Some Example shapes and their plots are shown below.
Note: After the transformation is done, the black dotted figure represents the old figure before tansformation, and the red figure is the new figure after transformation.

In the case of a circle, options that are available are :
1) R deg (rx) (ry)
2) S sr
3) T dx (dy)
4) P
 
 In the case of a polygon, options that are available are :
1) R deg (rx) (ry)
2) S sx (sy)
3) T dx (dy)
4) P
 
 Note : the properties that are inside the parenthesis are optional.
 
## Let say we have a circle having radius 3 and centred at (2,2).

<img width="466" alt="Screenshot 2021-05-22 at 10 19 13" src="https://user-images.githubusercontent.com/55681638/119215360-d2ff6a80-baea-11eb-89d1-aef9046aaaaf.png">

Then we rotate this circle by 145° anticlockwise and the axis of rotation is (1,1)

<img width="451" alt="Screenshot 2021-05-22 at 10 19 19" src="https://user-images.githubusercontent.com/55681638/119215492-a1d36a00-baeb-11eb-8776-8fe71b3843aa.png">

Then let say we want to scale it by a factor 1.5

<img width="442" alt="Screenshot 2021-05-22 at 10 19 25" src="https://user-images.githubusercontent.com/55681638/119215518-cf201800-baeb-11eb-9f4b-fe7ab7ffbe2e.png">

Then let say we want to translate it by +2 along x axis and +3 along y axis

<img width="444" alt="Screenshot 2021-05-22 at 10 19 29" src="https://user-images.githubusercontent.com/55681638/119215541-f37bf480-baeb-11eb-8a74-adff731cc96e.png">


## Now let's have a pentagon with vertices at : (2,1), (4,1), (5,2), (3,3) and (1,2)

<img width="472" alt="Screenshot 2021-05-22 at 10 59 10" src="https://user-images.githubusercontent.com/55681638/119215738-42765980-baed-11eb-9f88-118071eb84cc.png">

Let say we translate it by -6 in x axis and +2 in y axis

<img width="470" alt="Screenshot 2021-05-22 at 11 01 41" src="https://user-images.githubusercontent.com/55681638/119215773-6a65bd00-baed-11eb-9c98-3c19a098921c.png">

Then say we scale it by a factor 2 in x axis anf by 3 in y axis

<img width="461" alt="Screenshot 2021-05-22 at 11 02 02" src="https://user-images.githubusercontent.com/55681638/119215812-aef15880-baed-11eb-80e7-8ed7e9c58118.png">

Then at last we rotate is by 55 degree along its centre

<img width="456" alt="Screenshot 2021-05-22 at 11 02 35" src="https://user-images.githubusercontent.com/55681638/119215866-00014c80-baee-11eb-9b44-2d48eb556020.png">

