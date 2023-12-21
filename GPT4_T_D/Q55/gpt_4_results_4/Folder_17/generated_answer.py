
def lists_with_product_equal_n(lst):
    output = []
    N = len(lst)
    for i in range(N):
        for j in range(i, N):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k % N]
                if product == 18:
                    output.append(lst[k % N for k in range(i, j + 1)])
                elif product > 18:
                    break
    return output
