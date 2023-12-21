
from collections import deque
import numpy as np

def lists_with_product_equal_n(lst):
    #Make lst circular
    circular_lst = deque(lst)
    circular_lst.extend(lst[:-1])

    #List to keep found sublists
    result = []

    for i in range(len(circular_lst) - len(lst) + 1):  #Slide through the circular list
        for j in range(i + 1, i + len(lst) + 1):  #Slide through the sublist
            sublist = list(circular_lst)[i:j]
            if np.prod(sublist) == 990:
                result.append(sublist)

    return result
