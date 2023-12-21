
def lists_with_product_equal_n(lst):
    n = len(lst)
    circular_list = lst + lst
    valid_sublists = []

    for i in range(n):
        for j in range(i+1, i+n+1):
            sublist = circular_list[i:j]
            product = 1
            for x in sublist:
                product *= x
            if product == 3:
                valid_sublists.append(sublist)
                
    return valid_sublists
