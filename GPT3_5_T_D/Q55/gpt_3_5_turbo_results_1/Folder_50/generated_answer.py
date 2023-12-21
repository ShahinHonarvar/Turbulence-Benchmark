
def lists_with_product_equal_n(lst):
    result = []
    product = 1
    start = 0
    end = 0
    
    while start < len(lst):
        if product == 45:
            result.append(lst[start:end + 1])
            product /= lst[start]
            start += 1
        elif end < start or product < 45:
            end += 1
            if end == len(lst):
                break
            product *= lst[end]
        else:
            product /= lst[start]
            start += 1

    return result
