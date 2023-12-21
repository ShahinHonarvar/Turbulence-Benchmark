
from itertools import permutations

def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    output_list = []
    circular_list += circular_list

    for i in range(size):
        for j in range(i+1, size+1):
            sublist = circular_list[i:j]
            product = 1
            for number in sublist:
                product *= number
            if product == -9:
                output_list.append(sublist)

    unique_output_list = [list(x) for x in set(tuple(x) for x in output_list)]
    
    return unique_output_list
