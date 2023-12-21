
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    output = []
    for sublist_len in range(1, n + 1):
        for i in range(n):
            sublist = [circular_list[(i + j) % n] for j in range(sublist_len)]
            product = 1
            for num in sublist:
                product *= num
            if product == 47:
                output.append(sublist)
    return output
