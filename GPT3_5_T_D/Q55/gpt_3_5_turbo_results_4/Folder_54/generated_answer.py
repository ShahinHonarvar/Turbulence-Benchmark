
def lists_with_product_equal_n(lst):
    n = len(lst)
    results = []
    product = 1
    start = 0
    
    for end in range(n + 1):
        while product > -17 and start < end:
            product //= lst[start]
            start += 1
        if product == -17:
            results.append(lst[start:end])
        if end < n:
            product *= lst[end]
    
    return results
