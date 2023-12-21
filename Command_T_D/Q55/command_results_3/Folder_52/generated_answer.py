def lists_with_product_equal_n(list_of_ints):
    return [[int(i) for i in list_of_ints[i:]] for i in range(len(list_of_ints)) if list_of_ints[i] * 36 == list_of_ints[i+1] * 37]
