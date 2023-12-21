
def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    product = 1
    start = 0
    
    for i in range(n * 2):
        if product == -779:
            result.append(circular_list[start:i % n])
        product //= circular_list[start]
        
        if i % n == start:
            start = (start + 1) % n
            product = 1
        else:
            product *= circular_list[i % n]
    
    return result
