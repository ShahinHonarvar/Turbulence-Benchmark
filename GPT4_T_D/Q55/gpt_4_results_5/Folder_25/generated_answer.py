
def lists_with_product_equal_n(clist):
    n = len(clist)
    ans = []
    for l in range(1, n + 1):
        for i in range(n):
            sublist = [clist[(i + j) % n] for j in range(l)]
            product = 1
            for num in sublist:
                product *= num
            if product == -32:
                ans.append(sublist)
    return ans
