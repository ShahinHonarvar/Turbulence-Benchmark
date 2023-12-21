
from collections import deque
from itertools import combinations

def lists_with_product_equal_n(circular_list):
    circle = deque(circular_list)
    lists = []

    for i in range(len(circular_list)):
        for r in range(1, len(circular_list)+1):
            sublist = list(circle)[0:r]
            temp = 1
            for num in sublist:
                temp *= num
            if temp == -16:
                lists.append(sublist)
                
        circle.rotate(1)
        
    return lists
