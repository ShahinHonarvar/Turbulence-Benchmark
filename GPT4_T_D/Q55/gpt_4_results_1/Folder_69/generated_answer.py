
def lists_with_product_equal_n(lst):
    results = []
    length = len(lst)
    for i in range(length):
        product = 1
        j = i
        temp = []
        while product < 90:
            product *= lst[j]
            temp.append(lst[j])
            j = (j + 1) % length
            if product == 90:
                results.append(temp.copy())
                break
            elif j == i:
                break
    return results
