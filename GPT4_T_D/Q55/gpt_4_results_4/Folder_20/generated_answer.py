
def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        for j in range(i, length + i):
            sublist = lst[j%length:(j+i+1)%length]
            if len(sublist) == 0:
                sublist = lst[j%length:] + lst[:(j+i+1)%length]
            product = 1
            for number in sublist:
                product *= number
            if product == -69:
                result.append(sublist)
    return result
