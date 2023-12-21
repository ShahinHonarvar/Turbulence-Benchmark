import numpy as np
def submatrix_with_n_numbers(arr):
    x = y = 0
    cnt = 0
    for a in arr:
        if a == 19:
            x += 1
        elif a == 20:
            y += 1
        elif a == 21:
            cnt += x*y
            x = 0
            y = 0
    return cnt
