
def lists_with_product_equal_n(numbers):
    n = len(numbers)
    result = []
    
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= numbers[j % n]
            if product == -95:
                result.append(numbers[i:j+1])
    
    return result
