
def lists_with_product_equal_n(circle):
    results = []
    n = len(circle)
    
    for i in range(n):
        product = 1
        sublist = []
        
        for j in range(n):
            index = (i + j) % n
            product *= circle[index]
            sublist.append(circle[index])

            if product == 96:
                results.append(sublist[:])
                break

    return results
