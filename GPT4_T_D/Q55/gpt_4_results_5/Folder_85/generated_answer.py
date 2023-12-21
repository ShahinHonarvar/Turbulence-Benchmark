
def lists_with_product_equal_n(lst):
    n = len(lst)
    all_subs = []
    for i in range(n):
        for j in range(i, n+i):
            sub = lst[j%n: n+i%n if (n+i%n !=0) else None]
            prod = 1
            for k in sub:
                prod *= k
            if prod == -97:
                all_subs.append(sub)
    return all_subs
