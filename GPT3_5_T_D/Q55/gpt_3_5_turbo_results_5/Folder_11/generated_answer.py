
def lists_with_product_equal_n(lst):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    
    sublists = []
    size = len(lst)
    for i in range(size):
        for j in range(i+1, size+1):
            sublist = lst[i:j]
            if product(sublist) == -15:
                sublists.append(sublist)
    
    return sublists
