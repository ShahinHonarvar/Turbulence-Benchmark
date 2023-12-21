
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = circular_list[start:end if end < n else end - n]
            product = 1
            for i in sublist:
                product *= i
            if product == -76:
                result.append(sublist)
    return result
