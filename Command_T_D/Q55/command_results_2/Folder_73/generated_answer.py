import math
def lists_with_product_equal_n(list1):
    res = []
    for i in range(1, len(list1) + 1):
        prod = 1
        j = 0
        while j < i:
            prod *= list1[j]
            j += 1
        if prod == 40:
            res += [[list1[j]] for j in range(i)]
    return res
