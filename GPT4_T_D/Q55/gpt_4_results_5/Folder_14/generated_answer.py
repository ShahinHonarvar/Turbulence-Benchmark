
def lists_with_product_equal_n(circular_list):
    n = -72
    length = len(circular_list)
    results = []
    for i in range(length):
        for j in range(i + 1, length + 1):
            sublist = circular_list[i:j] if j <= length else circular_list[i:] + circular_list[:(j % length)]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                results.append(sublist)
    return results
