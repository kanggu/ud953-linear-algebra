print("Quiz: Plus, Minus, Scalar Multiply")
# 1
myVector1 = Vector([8.218, -9.341])
myVector2 = Vector([-1.129, 2.111])
print("# 1: ", myVector1 + myVector2)

# 2
myVector1 = Vector([7.119, 8.215])
myVector2 = Vector([-8.223, 0.878])
print("# 2: ", myVector1 - myVector2)

# 3
scalar1 = 7.41
myVector1 = Vector([1.671, -1.102, -0.318])
print("# 3: ", scalar1 * myVector1)


print("Quiz: Magnitude & Direction")
# 1
myVector1 = Vector([-0.221, 7.437])
print("# 1: {}".format(myVector1.magnitude()))

# 2
myVector1 = Vector([8.813, -1.331, -6.247])
print("# 2: {}".format(myVector1.magnitude()))

# 3
myVector1 = Vector([5.581, -2.136])
print("# 3: ", myVector1.direction())

# 4
myVector1 = Vector([1.996, 3.108, -4.554])
print("# 4: ", myVector1.direction())


print("Quiz: Dot Product and Angle")
# 1
myVector1 = Vector([7.887, 4.138])
myVector2 = Vector([-8.802, 6.776])
print("# 1: {}".format(myVector1 * myVector2))

# 2
myVector1 = Vector([-5.955, -4.904, -1.874])
myVector2 = Vector([-4.496, -8.755, 7.103])
print("# 2: {}".format(myVector1 * myVector2))

# 3
myVector1 = Vector([3.183, -7.627])
myVector2 = Vector([-2.668, 5.139])
print("# 3: {} rad".format(myVector1.angle(myVector2)))

# 4
myVector1 = Vector([7.35, 0.221, 5.188])
myVector2 = Vector([2.751, 8.259, 3.985])
print("# 4: {} deg".format(myVector1.angle(myVector2, True)))


print("Quiz: Checking for Parallelism & Orthogonality")
# 1
myVector1 = Vector([-7.579, -7.88])
myVector2 = Vector([22.737, 23.64])
print("# 1: Parallel - {}".format(myVector1.isParallel(myVector2)))
print("# 1: Orthogonal - {}".format(myVector1.isOrthogonal(myVector2)))

# 2
myVector1 = Vector([-2.029, 9.97, 4.172])
myVector2 = Vector([-9.231, -6.639, -7.245])
print("# 2: Parallel - {}".format(myVector1.isParallel(myVector2)))
print("# 2: Orthogonal - {}".format(myVector1.isOrthogonal(myVector2)))

# 3
myVector1 = Vector([-2.328, -7.284, -1.214])
myVector2 = Vector([-1.821, 1.072, -2.94])
print("# 3: Parallel - {}".format(myVector1.isParallel(myVector2)))
print("# 3: Orthogonal - {}".format(myVector1.isOrthogonal(myVector2)))

# 4
myVector1 = Vector([2.118, 4.827])
myVector2 = Vector([0, 0])
print("# 4: Parallel - {}".format(myVector1.isParallel(myVector2)))
print("# 4: Orthogonal - {}".format(myVector1.isOrthogonal(myVector2)))


print("Quiz: Projecting Vectors")
# 1
myVector1 = Vector([3.039, 1.879])
myVector2 = Vector([0.825, 2.036])
print("# 1: Parallel Projection")
print(myVector1.parallelProjection(myVector2))

# 2
myVector1 = Vector([-9.88, -3.264, -8.159])
myVector2 = Vector([-2.155, -9.353, -9.473])
print("# 2: Orthogonal Projection")
print(myVector1.orthogonalProjection(myVector2))

# 3
myVector1 = Vector([3.009, -6.172, 3.692, -2.51])
myVector2 = Vector([6.404, -9.144, 2.759, 8.718])
print("# 3: Parallel Projection")
print(myVector1.parallelProjection(myVector2))
print("# 3: Orthogonal Projection")
print(myVector1.orthogonalProjection(myVector2))


print("Quiz: Cross Product")
# 1
myVector1 = Vector([8.462, 7.893, -8.187])
myVector2 = Vector([6.984, -5.975, 4.778])
print("# 1: ", myVector1.cross(myVector2))

# 2
myVector1 = Vector([-8.987, -9.838, 5.031])
myVector2 = Vector([-4.268, -1.861, -8.866])
print("# 2: Parallelogram area - {}".format(myVector1.cross(myVector2).magnitude()))

# 3
myVector1 = Vector([1.5, 9.547, 3.691])
myVector2 = Vector([-6.007, 0.124, 5.772])
print("# 3: Triangle area - {}".format(myVector1.cross(myVector2).magnitude() / 2))
