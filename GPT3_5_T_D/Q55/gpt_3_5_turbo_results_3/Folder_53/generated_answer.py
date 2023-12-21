
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= circular_list[(i + j) % n]
            if product == -87:
                result.append(circular_list[i : i + j + 1])
    return result
