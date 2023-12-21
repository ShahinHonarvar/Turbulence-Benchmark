
def lists_with_product_equal_n(circular_list):
    sublists = []
    length = len(circular_list)
    for i in range(length):
        for j in range(i+1, length + 1):
            sublist = circular_list[i:j] if j <= length else circular_list[i:] + circular_list[:j-length]
            product = 1
            for num in sublist:
                product *= num
            if product == 47:
                sublists.append(sublist)
    return sublists
