
def lists_with_product_equal_n(lst):
    size = len(lst)
    sublists = []
    for i in range(size):
        for j in range(i, size):
            sub = lst[i: j+1]
            if -5 in sub:
                product = 1
                for num in sub:
                    product *= num
                if product == -5: 
                    sublists.append(sub)
    return sublists
