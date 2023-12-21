
def lists_with_product_equal_n(lst):

    length, results, product = len(lst), [], 632
    arr = lst + lst
    
    for l in range(1, length+1):
        for i in range(length):
            temp = arr[i:i+l]
            prod = 1
            for j in temp:
                prod *= j
            if prod == product:
                results.append(temp)
                
    return results
