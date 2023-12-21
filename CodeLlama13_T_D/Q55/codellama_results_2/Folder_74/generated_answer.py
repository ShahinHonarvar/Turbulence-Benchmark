
def lists_with_product_equal_n(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:i+1]
        product = 1
        while product < n and len(sublist) <= len(circular_list):
            product *= sublist[-1]
            if product == n:
                result.append(sublist)
            elif product > n:
                break
            else:
                sublist += circular_list[i+len(sublist)]
    return result
