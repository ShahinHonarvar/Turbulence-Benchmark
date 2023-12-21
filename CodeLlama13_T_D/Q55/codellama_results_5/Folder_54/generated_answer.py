
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            if product(lst[i:j]) == -17:
                result.append(lst[i:j])
    return result
