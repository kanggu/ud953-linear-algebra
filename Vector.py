import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

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
            return self.dot(x)
        else:
            return Vector([x * i for i in self.coordinates])

    def __rmul__(self, n):
        return self.__mul__(n)

    def magnitude(self):
        return math.sqrt(sum([i ** 2 for i in self.coordinates]))

    def __truediv__(self, n):
        return Vector([i / n for i in self.coordinates])

    def direction(self): # unit vector, normalized vector
        try:
            return self / self.magnitude()
        except ZeroDivisionError:
            raise Exception("Cannot normalize zero vector.")

    def dot(self, v):
        return sum([i * j for i,j in zip(self.coordinates,v.coordinates)])

    def angle(self, v, inDegree=False):
        try:
            if self.isZero() or v.isZero():
                raise ZeroVectorError
            else:
                angle = math.acos(self.direction() * v.direction())
                if inDegree:
                    return angle * 180 / math.pi
                else:
                    return angle
        except ZeroVectorError:
            raise ZeroVectorError("This function is not valid with zero vector.")

    def isZero(self, tolerance = 1e-10): # if is zero vector
        return self.magnitude() < tolerance

    def isParallel(self, v):
        return (self.isZero() or v.isZero() or
                self.angle(v) == 0 or self.angle(v) == math.pi)

    def isOrthogonal(self, v, tolerance=1e-10):
        return abs(self * v) < tolerance

    def parallelProjection(self, v):
        try:
            if self.isZero() or v.isZero():
                raise ZeroVectorError
            else:
                return self * v.direction() * v.direction()
        except ZeroVectorError:
            raise ZeroVectorError("This function is not valid with zero vector")

    def orthogonalProjection(self, v):
        return self - self.parallelProjection(v)

    def cross(self, v):
        arrCross = [self.coordinates[1] * v.coordinates[2] - self.coordinates[2] * v.coordinates[1],
                    self.coordinates[2] * v.coordinates[0] - self.coordinates[0] * v.coordinates[2],
                    self.coordinates[0] * v.coordinates[1] - self.coordinates[1] * v.coordinates[0]]
        return Vector(arrCross)
