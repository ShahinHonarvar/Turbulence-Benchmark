
def lists_with_product_equal_n(circular_list):
    sublists = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for i in range(length):
            num = circular_list[(start + i) % length]
            product *= num
            if product == -36:
                sublists.append(circular_list[start:start+i+1])
    return sublists
