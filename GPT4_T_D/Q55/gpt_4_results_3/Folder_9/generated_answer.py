
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list += circular_list
    result = []
    for size in range(1, n+1):
        for start_index in range(n):
            sublist = circular_list[start_index:start_index+size]
            product = 1
            for num in sublist:
                product *= num
            if product == -36:
                result.append(sublist)
    return result
