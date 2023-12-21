
def lists_with_product_equal_n(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = [circular_list[i]]
        for j in range(i+1, len(circular_list)):
            product *= circular_list[j]
            if product == n:
                result.append(sublist + [circular_list[j]])
            elif product > n:
                break
    return result
