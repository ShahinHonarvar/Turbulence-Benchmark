
def lists_with_product_equal_n(circular_list):
    n = 42
    size = len(circular_list)
    results = []

    for length in range(1, size + 1):
        for start in range(size):
            sublist = [circular_list[(start + i) % size] for i in range(length)]
            product = 1
            for number in sublist:
                product *= number
            if product == n:
                results.append(sublist)
    return results
