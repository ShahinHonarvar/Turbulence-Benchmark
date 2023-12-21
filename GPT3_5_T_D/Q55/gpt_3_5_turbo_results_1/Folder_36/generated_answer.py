
def lists_with_product_equal_n(lst):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    sublists = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            if product(lst[i:j]) == 714:
                sublists.append(lst[i:j])

    return sublists
