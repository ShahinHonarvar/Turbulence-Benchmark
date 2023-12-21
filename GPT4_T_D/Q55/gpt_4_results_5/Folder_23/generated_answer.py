
def lists_with_product_equal_n(lst):
    sub_lists = []
    N = len(lst)
    for i in range(N):
        for j in range(i, N+i):
            subset = lst[j%N:j%N+(i+1)%N]
            product = 1
            for x in subset:
                product *= x
            if product == -95:
                sub_lists.append(subset)
    return sub_lists
