
def lists_with_product_equal_n(lst):
    from itertools import cycle
    n, res = len(lst), []
    circ_list = cycle(lst)
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = [next(circ_list) for _ in range(end - start)]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == 714:
                res.append(sublist)
        for _ in range(start + 1, start + n + 1):
            next(circ_list)
    return res
