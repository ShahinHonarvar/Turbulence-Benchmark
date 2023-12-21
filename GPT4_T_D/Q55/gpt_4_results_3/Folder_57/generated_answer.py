
def lists_with_product_equal_n(circular_list):
    lst = circular_list*2
    n = len(circular_list)
    l = []
    for i in range(n):
        for j in range(i+1, i+n+1):
            product = 1
            for k in range(i, j):
                product *= lst[k]
                if product == -75:
                    l.append(lst[i:j])
                    break
                elif product > 75 or product < -75:
                    break
    return l
