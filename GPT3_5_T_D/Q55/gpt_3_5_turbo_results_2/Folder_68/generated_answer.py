 
def lists_with_product_equal_n(lst):
    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product

    sublists = []
    n = len(lst)

    for i in range(n):
        product = 1
        for j in range(i, i + n):
            index = j if j < n else j - n
            product *= lst[index]
            if product == 6:
                sublists.append(lst[i:index + 1])
                break

    return sublists
