
def lists_with_product_equal_n(numbers):
    n = len(numbers)
    target = -51
    result = []
    
    for i in range(n):
        product = 1
        
        for j in range(i, i+n):
            product *= numbers[j%n]
            
            if product == target:
                sublist = numbers[i:j%n+1]
                result.append(sublist)
    
    return result
