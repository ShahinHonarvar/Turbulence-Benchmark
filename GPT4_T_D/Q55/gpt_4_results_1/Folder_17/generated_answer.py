
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list += circular_list[:-1]
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = circular_list[start:end]
            product = 1
            for num in sublist:
                if num != 0:
                    product *= num
            if product == 18:
                result.append(sublist)
    return result
