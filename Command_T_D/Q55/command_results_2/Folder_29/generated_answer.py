def lists_with_product_equal_n(lst):
    result = []
    for i in range(1, len(lst)):
        j = i
        while j < len(lst) and lst[i] * lst[j] == 15:
            j += 1
        if j > i:
            result += [[lst[i:j]]]
    return result
