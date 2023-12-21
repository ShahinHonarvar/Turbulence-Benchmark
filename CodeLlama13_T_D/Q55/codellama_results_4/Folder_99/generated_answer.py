
def lists_with_product_equal_n(my_list, n):
    result = []
    for i in range(len(my_list)):
        prod = 1
        temp = my_list[i:] + my_list[:i]
        for j in temp:
            prod *= j
            if prod == n:
                result.append(temp)
                break
    return result
