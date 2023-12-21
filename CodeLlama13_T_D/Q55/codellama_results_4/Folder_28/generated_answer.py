
def lists_with_product_equal_n(list):
    result = []
    for i in range(len(list)):
        product = 1
        sublist = [list[i]]
        j = (i + 1) % len(list)
        while j != i:
            product *= list[j]
            if product == n:
                result.append(sublist)
            sublist.append(list[j])
            j = (j + 1) % len(list)
    return result
