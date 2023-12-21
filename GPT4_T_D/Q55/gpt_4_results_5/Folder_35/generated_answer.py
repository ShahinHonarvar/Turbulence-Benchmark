
def lists_with_product_equal_n(circular_list):
    result = []
    list_length = len(circular_list)
    for i in range(list_length):
        for j in range(i+1, i+list_length+1):
            sub_list = circular_list[i:j] if j <= list_length else circular_list[i:] + circular_list[:j-list_length]
            product = 1
            for num in sub_list:
                product *= num
            if product == 83:
                result.append(sub_list)
    return result
