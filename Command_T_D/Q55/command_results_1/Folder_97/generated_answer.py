import sys
def lists_with_product_equal_n(list1):
    if not list1:
        return []
    if len(list1) == 1:
        return [[-938]]
    res = []
    i = 0
    while i < len(list1):
        j = i
        while j < len(list1) and list1[i] * list1[j] == -938:
            j += 1
        res += [[list1[i:j]]
        i = j
    return res
