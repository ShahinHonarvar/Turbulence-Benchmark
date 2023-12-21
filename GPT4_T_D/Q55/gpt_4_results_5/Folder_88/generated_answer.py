
def lists_with_product_equal_n(lst):
    n = len(lst)
    lst += lst
    result = []
   
    for sublist_len in range(1, n+1):
        for i in range(n):
            sublist = lst[i:i+sublist_len]
            product = 1
            for num in sublist:
                product *= num
            if product == -56:
                result.append(sublist)
    return result
