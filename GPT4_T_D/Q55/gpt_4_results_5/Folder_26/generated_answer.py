
def lists_with_product_equal_n(lst):
    n = 93
    size = len(lst)
    result = []
    
    for x in range(size):
        for y in range(1, size + 1):
            sub_lst = lst[x:y] + lst[0:(y if y <= x else x)]
            product = 1
            for num in sub_lst:
                product *= num
            if product == n:
                result.append(sub_lst)
    return result
