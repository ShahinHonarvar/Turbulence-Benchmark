 
def lists_with_product_equal_n(lst):
    def calculate_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product

    results = []
    size = len(lst)
    for i in range(size):
        for j in range(i+1, size+1):
            sublist = lst[i:j]
            if calculate_product(sublist) == -97:
                results.append(sublist)
    return results
