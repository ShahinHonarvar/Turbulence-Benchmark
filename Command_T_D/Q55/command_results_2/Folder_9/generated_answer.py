def lists_with_product_equal_n(int_list):
    for i in range(1, len(int_list)):
        x = int_list[:i] + int_list[i:]
        if x:
            if x[0] == -36:
                yield x
    for i in range(1, len(int_list)):
        x = int_list[:i] + int_list[i+1:]
        if x:
            if x[0] == -36:
                yield x
