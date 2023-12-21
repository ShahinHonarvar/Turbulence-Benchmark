
def lists_with_product_equal_n(circular_list):
    def get_products(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product

    sublists = []
    for i in range(len(circular_list)):
        for j in range(i+1, len(circular_list)+1):
            if get_products(circular_list[i:j]) == 10:
                sublists.append(circular_list[i:j])
                
    return sublists
