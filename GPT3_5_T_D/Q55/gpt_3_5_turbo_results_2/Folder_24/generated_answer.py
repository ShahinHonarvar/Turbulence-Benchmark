
def lists_with_product_equal_n(circular_list):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    sublists = []
    length = len(circular_list)

    for size in range(1, length + 1):
        for start in range(length):
            end = start + size
            if end > length:
                sublist = circular_list[start:] + circular_list[:end % length]
            else:
                sublist = circular_list[start:end]

            if product(sublist) == -89:
                sublists.append(sublist)

    return sublists
