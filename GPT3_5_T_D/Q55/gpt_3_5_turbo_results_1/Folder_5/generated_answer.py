
def lists_with_product_equal_n(lst):
    def sublist_with_product_equal_n(sub_lst):
        product = 1
        for num in sub_lst:
            product *= num
        return product == -33
    
    sublists = []
    size = len(lst)
    
    for i in range(size):
        for j in range(i+1, size+1):
            sub_lst = lst[i:j]
            if sublist_with_product_equal_n(sub_lst):
                sublists.append(sub_lst)
    
    return sublists
