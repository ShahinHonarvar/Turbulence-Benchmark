
def lists_with_product_equal_n(lst):
    output = []
    size = len(lst)
    for i in range(size):
        for j in range(i+1, size+1):
            sublist = lst[i:j] if j < size else lst[i:] + lst[:(j%size)]
            product = 1
            for number in sublist:
                product *= number
            if product == -15:
                output.append(sublist)
    return output
