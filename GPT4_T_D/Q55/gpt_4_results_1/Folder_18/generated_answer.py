
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    
    for i in range(n):
        prod = 1
        j = i
        temp_lst = []
        while prod < 36:
            temp_lst.append(lst[j])
            prod *= lst[j]
            j = (j + 1)%n
        if prod == 36:
            result.append(temp_lst)
    return result
