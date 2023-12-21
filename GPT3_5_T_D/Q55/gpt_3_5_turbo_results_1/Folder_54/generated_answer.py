
def lists_with_product_equal_n(lst):
    n = len(lst)
    product = 1
    for i in range(n):
        product *= lst[i]
    
    result = []
    if product == -17:
        result.append(lst)
    
    for i in range(n):
        temp = lst.copy()
        temp.append(temp[0])
        temp.pop(0)
        product //= lst[i]
        product *= temp[i]
        if product == -17:
            result.append(temp[:i+1])
    
    return result
