
def lists_with_product_equal_n(circular_list):
    def sublist_with_product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == -95
        
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j+1]
            if sublist_with_product_equal_n(sublist):
                sublists.append(sublist)
    return sublists
