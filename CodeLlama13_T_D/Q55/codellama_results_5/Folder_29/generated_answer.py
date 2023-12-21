
def lists_with_product_equal_n(my_list):
    result = []
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            product = 1
            for k in range(i, j):
                product *= my_list[k]
            if product == 15:
                result.append(my_list[i:j])
    return result
