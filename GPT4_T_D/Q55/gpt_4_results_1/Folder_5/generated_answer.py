
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            sub_list = lst[i:j] 
            product = 1
            for elem in sub_list:
                product *= elem
            if product == -33:
                result.append(sub_list)
    return result
