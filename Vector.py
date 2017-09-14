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

    def __mul__(self, n):
        return Vector([n * i for i in self.coordinates])

    def __rmul__(self, n):
        return self.__mul__(n)

myVector1 = Vector([1,2,3])
myVector2 = Vector([4,5,6])
print(myVector1 + myVector2)
