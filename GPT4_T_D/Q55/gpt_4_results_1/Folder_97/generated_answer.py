
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    res = []
    for i in range(n):
        for j in range(i, n+i):
            sublist = circular_list[j%n:(j%n)+1] + circular_list[i:(j%n)%n]
            
            product = 1
            for num in sublist:
                product *= num
            if product == -938:
                res.append(sublist)
    return res
