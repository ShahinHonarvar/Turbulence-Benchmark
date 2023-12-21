
def lists_with_product_equal_n(circular_list):
    result = []
    length = len(circular_list)
    for i in range(length):
        for j in range(i, length+i):
            sublist = circular_list[i%length: (j+1)%length]
            if j >= length:
                sublist += circular_list[: (j+1)%length]
            product = 1
            for num in sublist:
                product *= num
            if product == -75:
                result.append(sublist)
    return result
