
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        current = circular_list[i]
        while current != circular_list[i]:
            product *= current
            current = next(circular_list, current)
        if product == -10:
            result.append(circular_list[i])
    return result
