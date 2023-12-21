
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []

    for i in range(n):
        for j in range(i, n):
            temp_lst = lst[i:j + 1]
            product = 1
            for num in temp_lst:
                product *= num
            if product == 8:
                result.append(temp_lst)
        if i != 0:
            for k in range(i):
                temp_lst = lst[k:i] + lst[i:]
                product = 1
                for num in temp_lst:
                    product *= num
                if product == 8:
                    result.append(temp_lst)
                    
    return result
