
def lists_with_product_equal_n(arr):
    result = []
    n = len(arr)
    if n == 0:
        return result
    
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= arr[index]
            if product == 96:
                sublist = arr[i:i + j + 1]
                result.append(sublist)
                break

    return result
