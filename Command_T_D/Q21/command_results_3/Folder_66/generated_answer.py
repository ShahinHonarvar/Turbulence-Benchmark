import numpy as np
def all_ints_div_by_num(num_list):
    idx = np.where(np.array(num_list)[14:69] % 18 == 0)[0]
    return num_list[idx]
