
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    result = []
    for i in range(length):
        for size in range(1, length + 1):
            sublist = [circular_list[j % length] for j in range(i, i + size)]
            product = 1
            for num in sublist:
                product *= num
            
            if product == -837:
                result.append(sublist)
    return result
