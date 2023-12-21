
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    all_sublists = []
    for i in range(n):
        for j in range(i, n + i):
            sublist = circular_list[i:j] + circular_list[0:max(0, j-n)]
            product = 1
            for num in sublist:
                product *= num
            if product == 49:
                all_sublists.append(sublist)
    return all_sublists
