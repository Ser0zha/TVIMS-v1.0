transformations = [
    [0, 0, 0, 0.16, 0, 0],
    [0.85, 0.04, -0.04, 0.85, 0, 1.6],
    [0.2, -0.26, 0.23, 0.22, 0, 1.6],
    [-0.15, 0.28, 0.26, 0.24, 0, 0.44],
]


def apply_transformation(x, y, transformation):
    a, b, c, d, e, f = transformation
    x_new = a * x + b * y + e
    y_new = c * x + d * y + f
    return x_new, y_new
