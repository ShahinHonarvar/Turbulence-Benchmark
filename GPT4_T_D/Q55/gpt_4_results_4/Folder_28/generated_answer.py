
from itertools import cycle

def lists_with_product_equal_n(circular_list):
    cycled_list = list(cycle(circular_list))
    result = []

    for i in range(len(circular_list)):
        for j in range(i + 1, i + len(circular_list) + 1):
            sublist = cycled_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 85:
                result.append(sublist)

    return result
