
def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i+1, i+n+1):
            sublist = circular_list[i:j] if j<=n else circular_list[i:] + circular_list[:j%n]
            product = 1
            for num in sublist:
                product *= num
            if product == -44:
                sublists.append(sublist)
    return sublists
