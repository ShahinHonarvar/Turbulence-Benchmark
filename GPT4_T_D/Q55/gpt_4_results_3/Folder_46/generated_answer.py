
def lists_with_product_equal_n(lst):
    circular_list = lst + lst
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            sublist = circular_list[i:j]
            product = 1
            for number in sublist:
                product *= number
            if product == 53:
                result.append(sublist)
    return result
