
def lists_with_product_equal_n(lst):
    n = 415
    length = len(lst)
    result = []
    
    for i in range(length):
        for j in range(i, length+i):
            product = 1
            for k in range(i, j+1):
                product *= lst[k%length]
                if product == n:
                    result.append(lst[i:k%length+1])
                elif product > n:
                    break
                    
    return result
