
def lists_with_product_equal_n(ls):
    n = len(ls)
    circular_ls = ls + ls
    res = []
    
    for size in range(1, n+1):
        for i in range(n):
            sublist = circular_ls[i:i+size]
            product = 1
            for num in sublist:
                product *= num
            if product == -87:
                res.append(sublist[:size])
    return res
