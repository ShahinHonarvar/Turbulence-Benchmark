
def lists_with_product_equal_n(lst):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    n = len(lst)
    target = 714
    result = []

    for i in range(n):
        for j in range(i, n):
            sub_lst = lst[i:j+1]
            if product(sub_lst) == target:
                result.append(sub_lst)

    return result
