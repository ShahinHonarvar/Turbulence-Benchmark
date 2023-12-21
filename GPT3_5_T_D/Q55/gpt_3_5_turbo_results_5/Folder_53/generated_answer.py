
def lists_with_product_equal_n(lst):
    n = len(lst)
    if n == 0:
        return []
    
    result = []
    product = 1
    start = 0
    
    for end in range(n):
        product *= lst[end]
        
        while product < -87:
            product //= lst[start]
            start += 1
        
        if product == -87:
            result.append(lst[start:end+1])
    
    return result
