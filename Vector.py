class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            self.magnitude = sum([i ** 2 for i in coordinates])

        except ValueError:
            raise ValueError("The coordinates must be nonempty")

        except TypeError:
            raise TypeError("The coordinates must be an iterable")


    def __str__(self):
        return "Vector: {}".format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


myVector1 = Vector([1,2,3])
print(myVector1.magnitude)
