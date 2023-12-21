def lists_with_product_equal_n(lst):
    return [[lst[i:j] for i in range(len(lst)) if j != i and list(map(int, lst[i:j])) == [ 415 ] ] for j in range(1, len(lst) + 1) if list(map(int, lst[i:j])) == [ 415 ] ]
