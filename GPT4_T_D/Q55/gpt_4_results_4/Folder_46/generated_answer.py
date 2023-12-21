
def lists_with_product_equal_n(circular_list):
    n = 53
    result = []
    length = len(circular_list)
    for sublist_size in range(1, length + 1):
        for index in range(length):
            sublist = circular_list[index: index + sublist_size] 
            if index + sublist_size > length: 
                sublist += circular_list[:(index+sublist_size)%length]
            prod = 1
            for i in sublist:
                prod *= i
            if prod == n:
                result.append(sublist)
    return result
