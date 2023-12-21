
def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[j % len(circular_list) : (j + i + 1) % len(circular_list)]
            if sublist == []:
                sublist = circular_list[j % len(circular_list) : ] + circular_list[ : (j + i + 1) % len(circular_list)]

            product = 1
            for number in sublist:
                product *= number

            if product == -54:
                if sublist not in sublists:
                    sublists.append(sublist)

    return sublists
