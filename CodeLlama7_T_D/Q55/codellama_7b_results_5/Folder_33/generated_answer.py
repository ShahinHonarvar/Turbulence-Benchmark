
def lists_with_product_equal_n(my_list):
    result = []
    for i in range(len(my_list)):
        current_product = 1
        for j in range(i, len(my_list)):
            current_product *= my_list[j]
            if current_product == -115:
                result.append(my_list[i:j+1])
    return result
