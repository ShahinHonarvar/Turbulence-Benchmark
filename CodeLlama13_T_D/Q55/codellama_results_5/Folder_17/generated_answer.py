
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = [lst[i]]
        for j in range(i+1, len(lst)):
            product *= lst[j]
            if product == n:
                result.append(sublist + [lst[j]])
            elif product > n:
                break
    return result
