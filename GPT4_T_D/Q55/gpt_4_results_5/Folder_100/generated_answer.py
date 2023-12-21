
from collections import deque

def lists_with_product_equal_n(lst):
    result_list = []
    lst = list(deque(lst))
    list_length = len(lst)
    
    for m in range(1, list_length+1):
        for n in range(list_length):
            temp_list = lst[n:n+m]
            if len(temp_list) < m:
                temp_list = temp_list + lst[:m-len(temp_list)]
            if product_of_list(temp_list) == 48:
                result_list.append(temp_list)
                
    return result_list

def product_of_list(lst):
    result = 1
    for ele in lst:
        result *= ele
    return result
