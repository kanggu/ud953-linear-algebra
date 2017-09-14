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

    def __mul__(self, n):
        return Vector([n * i for i in self.coordinates])

    def __rmul__(self, n):
        """ Called if 4*self for instance """
        return self.__mul__(n)


myVector1 = Vector([1,2,3])
myVector2 = Vector([1,2,3])
print(myVector1 * 2)
