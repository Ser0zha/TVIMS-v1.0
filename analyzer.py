import numpy as np


def compute_statistics(xs, ys):
    mean_x = np.mean(xs)
    mean_y = np.mean(ys)
    var_x = np.var(xs)
    var_y = np.var(ys)
    corr = np.corrcoef(xs, ys)[0, 1]

    return {
        'mean_x': mean_x,
        'mean_y': mean_y,
        'var_x': var_x,
        'var_y': var_y,
        'correlation': corr,
    }
