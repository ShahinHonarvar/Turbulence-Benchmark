
def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        j = i
        while product <= 90:
            product *= circular_list[j]
            if product == 90:
                result.append(circular_list[i:j+1])
            j = (j + 1) % n
    return result
