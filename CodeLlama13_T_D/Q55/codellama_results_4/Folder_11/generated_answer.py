
def lists_with_product_equal_n(circular_list, n):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        start = i
        while product != n:
            if start == len(circular_list):
                start = 0
            product *= circular_list[start]
            sublists.append([circular_list[i], circular_list[start]])
            start += 1
    return sublists
