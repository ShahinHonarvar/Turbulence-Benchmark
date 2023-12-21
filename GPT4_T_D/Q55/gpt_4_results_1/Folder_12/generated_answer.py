
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    output = []
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j+1] + circular_list[:max(0, (i + j + 1) - n)]
            product = 1
            for num in sublist:
                product *= num
            if product == -18:
                output.append(sublist)
    return output
