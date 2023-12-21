
def lists_with_product_equal_n(lst):
    size = len(lst)
    result = []
    for i in range(size):
        for j in range(i+1,size+1):
            sublist = lst[i:j]
            if j==size and i!=0:
                sublist += lst[0:i]
            product = 1
            for num in sublist:
                product *= num
            if product == 18:
                result.append(sublist)
    return result
