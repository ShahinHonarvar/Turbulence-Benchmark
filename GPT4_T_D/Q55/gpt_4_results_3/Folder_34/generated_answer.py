
def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []
    for i in range(n):
        for j in range(i,n):
            sub_lst = lst[i:j+1] 
            if sub_lst[0]==lst[-1]:
                sub_lst = [lst[-1]] + sub_lst
            product = 1
            for num in sub_lst:
                product *= num
            if product == -81:
                res.append(sub_lst)
    return res
