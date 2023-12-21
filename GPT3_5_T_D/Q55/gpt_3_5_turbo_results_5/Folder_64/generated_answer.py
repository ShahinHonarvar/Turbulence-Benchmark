
def lists_with_product_equal_n(lst):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    n = len(lst)
    sublists = []
    for i in range(n):
        for j in range(i+1, n+1):
            if product(lst[i:j]) == 3:
                sublists.append(lst[i:j])
    return sublists
