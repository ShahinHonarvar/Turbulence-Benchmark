
def lists_with_product_equal_n(numbers):
    result = []
    size = len(numbers)
    for i in range(size):
        product = 1
        for j in range(i, size + i):
            product *= numbers[j % size]
            if product == -22:
                result.append(numbers[i:j % size + 1])
    return result
