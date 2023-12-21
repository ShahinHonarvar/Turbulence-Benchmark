import numpy as np
def all_ints_div_by_num(lst):
    lst = np.array(lst)
    return np.where(np.all(lst == -858, axis=1))[0]
