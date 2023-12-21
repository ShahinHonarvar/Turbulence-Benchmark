
def lists_with_product_equal_n(circular_list, n):
    if len(circular_list) == 0:
        return []
    
    result = []
    for i in range(len(circular_list)):
        sublist = [circular_list[i]]
        product = circular_list[i]
        j = (i + 1) % len(circular_list)
        while j != i:
            if product * circular_list[j] == n:
                result.append(sublist + [circular_list[j]])
            elif product * circular_list[j] > n:
                break
            else:
                sublist.append(circular_list[j])
                product *= circular_list[j]
            j = (j + 1) % len(circular_list)
    
    return result
