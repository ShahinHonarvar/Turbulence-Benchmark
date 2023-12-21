
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []

    for size in range(1, n + 1):
        for i in range(0, n):
            sublist = [lst[(i + j) % n] for j in range(size)]
            product = 1
            for num in sublist:
                product *= num

            if product == -22:
                result.append(sublist)

    return result
