
def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        temp_list = []
        for j in range(i, len(circular_list)):
            temp_list.append(circular_list[j])
            product *= circular_list[j]
            if product == -115:
                sublists.append(temp_list)
                break
        else:
            continue
    return sublists
