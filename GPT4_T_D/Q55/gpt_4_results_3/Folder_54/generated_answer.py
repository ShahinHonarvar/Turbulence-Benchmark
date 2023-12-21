
def lists_with_product_equal_n(circular_list):
    result = []
    length = len(circular_list)
    circular_list.extend(circular_list)
    for i in range(length):
        for j in range(i+1, i+length+1):
            sublist = circular_list[i:j]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == -17:
                result.append(sublist)
    return result
