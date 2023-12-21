
def lists_with_product_equal_n(circle):
    result = []
    for i in range(len(circle)):
        prod = 1
        sublist = [circle[i]]
        for j in range(i+1, len(circle)):
            prod *= circle[j]
            if prod == n:
                result.append(sublist + [circle[j]])
                break
            elif prod > n:
                break
    return result
