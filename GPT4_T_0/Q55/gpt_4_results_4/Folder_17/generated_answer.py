
def lists_with_product_equal_n(circular_list):
    n = 18
    length = len(circular_list)
    result = []
    for i in range(length):
        for j in range(i, length):
            sublist = circular_list[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
        circular_list.append(circular_list.pop(0))
    return result
