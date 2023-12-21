
def lists_with_product_equal_n(circular_list):
    product = 1
    sublists = []
    for i in range(len(circular_list)):
        if product == -10:
            sublists.append(circular_list[i-len(sublist)+1:i+1])
        elif product > -10:
            return []
        else:
            product *= circular_list[i]
    return sublists
