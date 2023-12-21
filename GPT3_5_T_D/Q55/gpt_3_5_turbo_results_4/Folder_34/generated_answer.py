
def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n+1):
            if -81 in [lst[k] for k in range(i, j)]:
                sublists.append(lst[i:j])
                
    return sublists
