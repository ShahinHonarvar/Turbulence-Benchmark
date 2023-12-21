
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n+1):
            sub_list = lst[i:j]
            product = 1
            for num in sub_list:
                product *= num
            if product == 733:
                result.append(sub_list)
    return result
