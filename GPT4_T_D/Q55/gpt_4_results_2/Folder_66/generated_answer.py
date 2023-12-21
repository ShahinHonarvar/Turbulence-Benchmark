
from itertools import combinations

def lists_with_product_equal_n(circle_list):
    len_circle_list = len(circle_list)
    circle_list += circle_list # Doubling to include all rotation of circular list
    result = []
    for size in range(1, len_circle_list+1):
        for start in range(len_circle_list):
            sublist = circle_list[start: start+size]
            product = 1
            for num in sublist:
                product *= num
            if product == 78:
                if sublist not in result and len(sublist) <= len_circle_list:
                    result.append(sublist)
    return result
