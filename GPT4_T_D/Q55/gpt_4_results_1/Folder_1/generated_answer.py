
def lists_with_product_equal_n(lst):
    size = len(lst)
    products = []
    for i in range(size):
        for j in range(i, size+i):
            sub_list = lst[j%size : j%size + (j-i+1)%size]
            product = 1
            for num in sub_list:
                product *= num
            if product == -51:
                products.append(sub_list)
    return products
