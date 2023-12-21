
from collections import deque
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    circular_list = deque(circular_list)
    sublists = []
  
    for i in range(length):
        for j in range(1, length+1):
            sublist = list(circular_list)[i: i + j]
            product = 1
            for num in sublist:
                product *= num
            if product == -906:
                sublists.append(sublist)
        circular_list.rotate(1)
    return sublists
