
def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    circular_list = circular_list * 2
    result = []

    for window_size in range(1, size + 1):
        for start in range(size):
            window = circular_list[start: start + window_size]
            product = 1
            for elem in window:
                product *= elem
            if product == 45:
                result.append(window)

    return result
