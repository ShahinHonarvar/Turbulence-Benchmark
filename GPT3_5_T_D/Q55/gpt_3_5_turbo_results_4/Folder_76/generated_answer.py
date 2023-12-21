
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    sublists = []
    
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j+1]
            if product(sublist) == 247:
                sublists.append(sublist)
    
    return sublists
