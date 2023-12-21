
def lists_with_product_equal_n(arr):
    result = []
    n = len(arr)
    
    for i in range(n):
        sublist_product = 1
        for j in range(i, i + n):
            sublist_product *= arr[j % n]
            if sublist_product == 28:
                result.append(arr[i:j % n + 1])
                
    return result
