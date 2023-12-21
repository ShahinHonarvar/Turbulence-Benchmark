
def lists_with_product_equal_n(circular_list):
    circular_list = circular_list + circular_list
    result = []
    for i in range(len(circular_list) // 2):
        for j in range(i+1, len(circular_list) // 2 + i + 1):
            temp_list = circular_list[i:j]
            product = 1
            for num in temp_list:
                product *= num
            if product == 51:
                result.append(temp_list)
    return result
