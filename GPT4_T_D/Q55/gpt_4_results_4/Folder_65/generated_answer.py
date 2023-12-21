
def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)

    # append tail to head to form circular list
    lst = lst + lst[:length-1]

    for i in range(length):
        for j in range(i+1, length+1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 46:
                result.append(sublist)

    return result
