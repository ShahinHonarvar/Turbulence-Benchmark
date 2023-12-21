
def lists_with_product_equal_n(circular_list):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    sublists = []
    size = len(circular_list)
    for i in range(size):
        for j in range(i, size):
            sublist = circular_list[i:j+1]
            if product(sublist) == 91:
                sublists.append(sublist)
    return sublists
