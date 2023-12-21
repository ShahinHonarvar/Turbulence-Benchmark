
def lists_with_product_equal_n(circular_list):
    n = 15
    length = len(circular_list)
    if length == 0:
        return []
    circular_list += circular_list
    result = []
    for sublist_length in range(1, length + 1):
        for i in range(length):
            sublist = circular_list[i:i + sublist_length]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result
