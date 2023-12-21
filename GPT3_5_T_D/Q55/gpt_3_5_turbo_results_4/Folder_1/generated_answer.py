
def lists_with_product_equal_n(lst):
    def product(nums):
        result = 1
        for num in nums:
            result *= num
        return result

    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            sub = lst[i:j+1]
            if product(sub) == -51:
                sublists.append(sub)
    return sublists
