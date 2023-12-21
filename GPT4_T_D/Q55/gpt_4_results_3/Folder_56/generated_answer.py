
def lists_with_product_equal_n(lst):
    output = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:(j+1)] + lst[:i] if j < i else lst[i:(j+1)]
            product = 1
            for num in sublist:
                product *= num
            if product == -65:
                output.append(sublist)
    return output
