
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    result = []
    for i in range(length):
        for j in range(i, i + length):
            sublist = circular_list[j % length:(j + length) % length]
            product = 1
            for num in sublist:
                product *= num
            if product == 247:
                result.append(sublist[:])
    return result
