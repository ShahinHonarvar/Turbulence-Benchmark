
def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for start in range(n):
        for length in range(1, n + 1):
            sublist = [lst[(start + i) % n] for i in range(length)]
            if len(sublist) > 0 and product(sublist) == -95:
                sublists.append(sublist)
    return sublists

def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p
