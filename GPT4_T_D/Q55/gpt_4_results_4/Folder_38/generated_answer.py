
from collections import deque

def lists_with_product_equal_n(circular_list):
    sublists = []

    for start_index in range(len(circular_list)):
        for end_index in range(start_index + 1, start_index + len(circular_list) + 1):
            sublist = circular_list[start_index:end_index]
            if len(sublist) > len(circular_list):
                sublist = sublist[:len(circular_list)]
            if len(sublist) == 0:
                continue
            
            product = 1
            for num in sublist:
                product *= num
                if product == -23:
                    sublists.append(sublist)
                    break
                if product % -23 != 0:
                    break
        circular_list.rotate(-1)

    return sublists
