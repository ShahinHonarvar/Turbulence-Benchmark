
def lists_with_product_equal_n(numbers):
    result = []
    n = len(numbers)
    
    for i in range(n):
        for j in range(i, n):
            sublist = numbers[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == 40:
                result.append(sublist)
    
    return result
