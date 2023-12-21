
def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n+i):
            sublist = lst[j%n: j%n + (j-i+1)%n]
            product = 1
            for number in sublist:
                product *= number
            if product == 42:
                sublists.append(sublist)
    return sublists
