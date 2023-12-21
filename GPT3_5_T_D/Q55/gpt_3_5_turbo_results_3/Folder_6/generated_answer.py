
def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    if size == 0:
        return result
    
    for i in range(size):
        for j in range(i, size):
            sub_lst = lst[i:j+1]
            product = 1
            for num in sub_lst:
                product *= num
            if product == 42:
                result.append(sub_lst)
    
    return result
