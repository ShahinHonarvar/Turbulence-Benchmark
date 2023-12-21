
from collections import deque


def lists_with_product_equal_n(cl):
    result_array = []
    l = len(cl)
    cl = list(deque(cl,i) for i in range(l))
    for ci in cl:
        product_array = []
        result_array_tmp = []
        product = 1
        for i in range(l):
            if product*ci[i] > 27:
                while len(product_array) > 0 and product*ci[i] > 27:
                    product = product // product_array[0]
                    product_array.pop(0)
            if product*ci[i] <= 27:
                product_array.append(ci[i])
                product *= ci[i]
            if product == 27:
                result_array_tmp.append(product_array.copy())
        result_array.extend(result_array_tmp)
    return result_array
