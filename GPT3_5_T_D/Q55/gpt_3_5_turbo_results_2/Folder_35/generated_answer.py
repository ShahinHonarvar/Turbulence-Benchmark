
def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= circular_list[end % size]
            if product == 83:
                result.append(circular_list[start:(end+1) % size])
    return result
