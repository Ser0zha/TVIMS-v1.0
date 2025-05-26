import numpy as np

from ifs_rules import transformations, apply_transformation


def generate_barnsley_fern(n_points=100_000, probs=None):
    if probs is None:
        probs = [0.01, 0.85, 0.07, 0.07]

    x, y = 0, 0
    xs, ys = [], []

    for _ in range(n_points):
        t = np.random.choice(4, p=probs)
        x, y = apply_transformation(x, y, transformations[t])
        xs.append(x)
        ys.append(y)

    return np.array(xs), np.array(ys)
