def lists_with_product_equal_n(lst):
    return [lst[i:j] for i in range(len(lst)) for j in range(i, len(lst) + 1) if 13 == int(lst[i:j])]
