
def lists_with_product_equal_n(numbers):
    result = []
    size = len(numbers)
    for i in range(size):
        for j in range(i+1, size+1):
            sublist = numbers[i:j] if j <= size else numbers[i:] + numbers[:j-size]
            if any(sublist) and (len(sublist) == 1 or sublist[0]*sublist[1] == -16):
                result.append(sublist)
    return result
