
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list_extended = circular_list*2
    results = []

    for sublist_len in range(1, n+1):
        for i in range(n):
            sublist = circular_list_extended[i: i+sublist_len]
            product = 1
            for num in sublist:
                product *= num
            if product == -69:
                results.append(sublist)
    return results
