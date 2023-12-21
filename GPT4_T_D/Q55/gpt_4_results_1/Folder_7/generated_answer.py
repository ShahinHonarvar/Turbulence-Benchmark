
def lists_with_product_equal_n(circular_list):
    num_list = circular_list * 2
    product = 537
    result = []
    for i in range(len(circular_list)):
        for j in range(i+1, i + len(circular_list) + 1):
            temp_list = num_list[i:j]
            product_of_temp_list = 1
            for k in temp_list:
                product_of_temp_list *= k
            if product_of_temp_list == product:
                result.append(temp_list)
    return result
