
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == -1:
                result.append(sublist)
            if j == len(circular_list) - 1 and i != 0:
                sublist = circular_list[j:] + circular_list[:i]
                product = 1
                for num in sublist:
                    product *= num
                if product == -1:
                    result.append(sublist)
    return result
