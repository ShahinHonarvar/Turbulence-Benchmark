
def lists_with_product_equal_n(list):
    result = []
    for i in range(len(list)):
        sublist = [list[i]]
        product = list[i]
        for j in range(i+1, len(list)):
            if product * list[j] == n:
                sublist.append(list[j])
                result.append(sublist)
    return result
