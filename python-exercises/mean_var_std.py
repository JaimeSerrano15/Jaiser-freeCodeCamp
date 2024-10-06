import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    ls = np.array(list)
    print(ls)

    mean_rows = [ls[[0, 1, 2]].mean(), ls[[3, 4, 5]].mean(), ls[[6, 7, 8]].mean()]
    mean_cols = [ls[[0, 3, 6]].mean(), ls[[1, 4, 7]].mean(), ls[[2, 5, 8]].mean()]

    vars_rows = [ls[[0, 1, 2]].var(), ls[[3, 4, 5]].var(), ls[[6, 7, 8]].var()]
    vars_cols = [ls[[0, 3, 6]].var(), ls[[1, 4, 7]].var(), ls[[2, 5, 8]].var()]

    std_rows = [ls[[0, 1, 2]].std(), ls[[3, 4, 5]].std(), ls[[6, 7, 8]].std()]
    std_cols = [ls[[0, 3, 6]].std(), ls[[1, 4, 7]].std(), ls[[2, 5, 8]].std()]

    max_rows = [ls[[0, 1, 2]].max(), ls[[3, 4, 5]].max()]
    max_cols = [ls[[0, 3, 6]].max(), ls[[1, 4, 7]].max()]

    min_rows = [ls[[0, 1, 2]].min(), ls[[3, 4, 5]].min()]
    min_cols = [ls[[0, 3, 6]].min(), ls[[1, 4, 7]].min()]

    sum_rows = [ls[[0, 1, 2]].sum(), ls[[3, 4, 5]].sum()]
    sum_cols = [ls[[0, 3, 6]].sum(), ls[[1, 4, 7]].sum()]

    return {
        'mean': [mean_cols, mean_rows, ls.mean()],
        'var': [vars_cols, vars_rows, ls.var()],
        'standard deviation': [std_cols, std_rows, ls.std()],
        'max': [max_cols, max_rows, ls.max()],
        'min': [min_cols, min_rows, ls.min()],
        'sum': [sum_cols, sum_rows, ls.sum()]
    }
