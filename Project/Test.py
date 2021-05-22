import unittest
import numpy as np
from unittest.mock import patch
import a3 as my

atolerance, rtolerance = 0.01, 0.01


class TestPolygon(unittest.TestCase):
    # P1 is the square and P2 a pentagon
    inp = np.array([[1.0, 1.0, 1.0], [1.0, 5.0, 1.0],
                    [5.0, 5.0, 1.0], [5.0, 1.0, 1.0]])
    P1 = my.Polygon(inp)
    inp2 = np.array([[2.0, 1.0, 1.0], [4.0, 1.0, 1.0], [
                    5.0, 2.0, 1.0], [3.0, 3.0, 1.0], [1.0, 2.0, 1.0]])
    P2 = my.Polygon(inp2)
    inp3 = np.array([[0.0, 0.0, 1.0], [4.0, 0.0, 1.0],
                     [4.0, 4.0, 1.0], [0.0, 4.0, 1.0]])
    P3 = my.Polygon(inp3)

    def test_1(self):
        print('test_1 starts')
        user_output = self.P1.rotate(90)
        exp_output = (np.array([1.0, 5.0, 5.0, 1.0]),
                      np.array([-1.0, -1.0, -5.0, -5.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_1 ends')

    def test_2(self):
        print('test_2 starts')
        user_output = self.P1.translate(2, 2)
        exp_output = (np.array([3.0, 7.0, 7.0, 3.0]),
                      np.array([1.0, 1.0, -3.0, -3.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_2 ends')

    def test_3(self):
        print('test_3 starts')
        user_output = self.P1.scale(3, 2)
        exp_output = (np.array([-1.0, 11.0, 11.0, -1.0]),
                      np.array([3.0, 3.0, -5.0, -5.0]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_3 ends')

    def test_4(self):
        print('test_4 starts')
        user_output = self.P2.scale(-2, -2)
        exp_output = (np.array([5.0, 1.0, -1.0, 3.0, 7.0]),
                      np.array([3.4, 3.4, 1.4, -0.6, 1.4]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_4 ends')

    def test_5(self):
        print('test_5 starts')
        user_output = self.P2.rotate(-45)
        exp_output = (np.array([1.13137085, -1.69705627, -1.69705627,  2.54558441,  3.95979797]),
                      np.array([5.93969696, 3.11126984, 0.28284271, 1.69705627, 5.93969696]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_5 ends')

    def test_6(self):
        print('test_6 starts')
        user_output = self.P2.scale(0.5, 0.3)
        exp_output = (np.array([0.98994949, -0.42426407, -0.42426407,  1.69705627,  2.40416306]),
                      np.array([4.15778787, 3.30925974, 2.4607316, 2.88499567, 4.15778787]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_6 ends')

    def test_7(self):
        print('test_7 starts')
        user_output = self.P3.rotate(45, 2, 2)
        exp_output = (np.array([-0.82842712,  2.0,  4.82842712,  2.0]),
                      np.array([2.0, -0.82842712,  2.0,  4.82842712]))
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_7 ends')


class TestCircle(unittest.TestCase):

    C1 = my.Circle(2.0, 2.0, 3.0)  # 2,2 is center and 3 is radius
    C2 = my.Circle(2.0, 2.0, 3.0)  # 2,2 is center and 3 is radius

    def test_1(self):
        print('test_1 starts')
        user_output = self.C1.rotate(45)
        exp_output = (2.8284271247461903, 0.0, 3.0)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_1 ends')

    def test_2(self):
        print('test_2 starts')
        user_output = self.C1.scale(0.5)
        exp_output = (2.8284271247461903, 0.0, 1.5)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_2 ends')

    def test_3(self):
        print('test_3 starts')
        user_output = self.C1.translate(-3, 3)
        exp_output = (-0.1715728752538097, 3.0, 1.5)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_3 ends')

    def test_4(self):
        print('test_4 starts')
        user_output = self.C2.rotate(45, 4, 4)
        exp_output = (1.1715728752538097, 4.0, 3.0)
        print(f'returned value {user_output}')
        print(f'expected value {exp_output}')
        np.testing.assert_allclose(exp_output, user_output, rtol=rtolerance, atol=atolerance)
        print('test_4 ends')

if __name__ == '__main__':
    unittest.main()
