
def lists_with_product_equal_n(numbers):
    result = []
    size = len(numbers)
    for i in range(size):
        for j in range(i, size):
            sublist = numbers[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == -115:
                result.append(sublist)
    return result
