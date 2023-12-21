
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    circular_list = circular_list + circular_list
    result = []
    for size in range(1, length+1):
        for index in range(length):
            sublist = circular_list[index:index+size]
            product = 1
            for num in sublist:
                product *= num
            if product == 4:
                result.append(sublist)
    return result
