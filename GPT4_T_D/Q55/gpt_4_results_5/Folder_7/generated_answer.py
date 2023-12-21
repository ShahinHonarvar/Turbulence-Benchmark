
def lists_with_product_equal_n(lst):
    size = len(lst)
    result = []
    for i in range(size):
        for j in range(i + 1, size + 1):
            sublist = lst[i:j] + lst[0:max(0, (j - size))]
            product = 1
            for num in sublist:
                product *= num
            if product == 537:
                result.append(sublist)
    return result
