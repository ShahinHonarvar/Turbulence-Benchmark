
def lists_with_product_equal_n(lst):
    def is_product(lst):
        product = 1
        for i in lst:
            product *= i
        return product == 5

    sublists = []
    n = len(lst)
    for start in range(n):
        for finish in range(start+1, start+n+1):
            if finish>n:
                sublist=lst[start:]+lst[:finish%n]
            else:
                sublist=lst[start:finish]
            if is_product(sublist):
                sublists.append(sublist)
    return sublists
