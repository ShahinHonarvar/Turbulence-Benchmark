
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    sublists = []

    for length in range(1, n+1):
        for start in range(n):
            sublist = [circular_list[(start + i) % n] for i in range(length)]
            product = 1
            for i in sublist:
                product *= i
            if product == -32:
                sublists.append(sublist)

    return sublists
