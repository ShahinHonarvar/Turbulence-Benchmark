
def lists_with_product_equal_n(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:i+n]
        if len(sublist) == n and prod(sublist) == n:
            result.append(sublist)
    return result
