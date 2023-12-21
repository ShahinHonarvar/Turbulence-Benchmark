
def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    circular_list += circular_list
    for i in range(n):
        for j in range(i+1, i+n+1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -91:
                result.append(sublist)
    return result
