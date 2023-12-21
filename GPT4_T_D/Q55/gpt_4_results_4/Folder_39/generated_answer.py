
def lists_with_product_equal_n(lst):
    rtn_lst = []
    size = len(lst)
    lst = 2*lst
    for i in range(size):
        for j in range(i+1, i+size+1):
            if j-i>size:
                break
            curr_lst = lst[i:j]
            product = 1
            for num in curr_lst:
                product *= num
            if product == -46:
                rtn_lst.append(curr_lst)
    return rtn_lst
