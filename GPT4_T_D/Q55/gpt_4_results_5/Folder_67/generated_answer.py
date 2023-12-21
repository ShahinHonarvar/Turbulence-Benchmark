
def lists_with_product_equal_n(circular_list):
    circular_list = circular_list + circular_list
    result = []
    length_list = len(circular_list) // 2
    for i in range(length_list):
        for j in range(i+1, i + length_list + 1):
            sublist = circular_list[i:j]
            product = 1
            for number in sublist:
                product *= number
            if product == 33:
                result.append(sublist)
    return result
