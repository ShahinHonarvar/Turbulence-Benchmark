
def lists_with_product_equal_n(circular_list):
    n = 74
    result = []
    length = len(circular_list)
    for i in range(length):
        for j in range(i, length):
            sublist = circular_list[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
        circular_list.append(circular_list[i])
    return result
