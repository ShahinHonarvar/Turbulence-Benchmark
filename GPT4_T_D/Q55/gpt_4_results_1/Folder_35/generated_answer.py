
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    circular_list += circular_list
    product_83_sublists = []
    for i in range(length):
        for j in range(i + 1, i + length + 1):
            sublist = circular_list[i:j]
            prod = 1
            for num in sublist:
                prod *= num
                if prod > 83:
                    break
            if prod == 83:
                product_83_sublists.append(sublist)
    return product_83_sublists
