
def lists_with_product_equal_n(lst):
    def products(lst):
        prods = []
        for i in range(len(lst)):
            for j in range(i+1, i+len(lst)):
                sub_list = lst[i:j]
                product = 1
                for num in sub_list:
                    product *= num
                if product == 45:
                    prods.append(sub_list)
        return prods
    
    return products(lst)
