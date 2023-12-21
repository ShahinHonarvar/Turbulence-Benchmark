
def lists_with_product_equal_n(circular_list):
    def product(lst):
        prod = 1
        for elem in lst:
             prod *= elem
        return prod

    sublists = []
    length = len(circular_list)
    for size in range(1,length+1):
        for start in range(0,length):
            sublist = circular_list[start:start+size]
            if start+size > length:
                sublist.extend(circular_list[0:(start+size)%length])
            if product(sublist) == 99:
                sublists.append(sublist)
    return sublists
