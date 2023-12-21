
from collections import deque

def lists_with_product_equal_n(circular_list):
    result = []
    list_len = len(circular_list)
    temp_product = 1
    for i in range(list_len * 2):
        j = i % list_len
        temp_product *= circular_list[j]
        temp_list = deque(circular_list[j])

        while temp_product > 415 and len(temp_list) > 0:
            temp_product //= temp_list.popleft()
            
        if temp_product == 415:
            result.append(list(temp_list))
            
    return result
