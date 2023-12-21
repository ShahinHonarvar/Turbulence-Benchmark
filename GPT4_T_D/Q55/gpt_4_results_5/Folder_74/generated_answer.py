
import itertools

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list += circular_list
    output_lists = []
    for i in range(n):
        for j in range(1, n + 1):
            if i + j > n:
                break
            sublist = circular_list[i:i+j]
            product = 1
            for val in sublist:
                product *= val
            if product == 51:
                output_lists.append(sublist)
    return output_lists
