
def lists_with_product_equal_n(list):
    result = []
    for i in range(len(list)):
        product = 1
        sublist = [list[i]]
        for j in range(i+1, len(list)):
            product *= list[j]
            if product == -93:
                result.append(sublist + [list[j]])
                break
            elif product > -93:
                break
    return result
