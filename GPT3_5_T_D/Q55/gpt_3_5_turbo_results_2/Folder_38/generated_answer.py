
def lists_with_product_equal_n(lst):
    results = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sub_lst = lst[i:j+1]
            product = 1
            for num in sub_lst:
                product *= num
            if product == -23:
                results.append(sub_lst)
    return results
