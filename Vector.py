import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            self.magnitude = math.sqrt(sum([i ** 2 for i in coordinates]))

        except ValueError:
            raise ValueError("The coordinates must be nonempty")

        except TypeError:
            raise TypeError("The coordinates must be an iterable")


    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        return Vector([i + j for i,j in zip(self.coordinates,v.coordinates)])

    def __sub__(self,v):
        return Vector([i - j for i,j in zip(self.coordinates, v.coordinates)])

    def __mul__(self, x):
        if type(x) == type(self):
            return self.inner(x)
        else:
            return Vector([x * i for i in self.coordinates])

    def __rmul__(self, n):
        return self.__mul__(n)

    def __truediv__(self, n):
        return Vector([i / n for i in self.coordinates])

    def direction(self): # unit vector
        return self / self.magnitude

    def inner(self, v):
        return sum([i * j for i,j in zip(self.coordinates,v.coordinates)])

    def angle(self, v):
        try:
            if self.isZero() or v.isZero():
                raise ZeroVectorError
            else:
                return math.acos(self * v / self.magnitude / v.magnitude)
        except ZeroVectorError:
            raise ZeroVectorError("This function is not valid with zero vector.")

    def isZero(self, tolerance = 1e-10):
        return self.magnitude < tolerance

    def isParallel(self, v):
        return (self.isZero() or v.isZero() or
                self.angle(v) == 0 or self.angle(v) == math.pi)

    def isOrthogonal(self, v, tolerance=1e-10):
        return self * v < tolerance

myVector1 = Vector([-2.328, -7.284, -1.214])
myVector2 = Vector([-1.821, 1.072, -2.94])
print(myVector1.isOrthogonal(myVector2))
print(myVector1 * myVector2)
