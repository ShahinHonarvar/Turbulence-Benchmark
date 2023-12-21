
def lists_with_product_equal_n(nums):
    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p

    sublists = []
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = nums[i:j]
            if product(sublist) == -41:
                sublists.append(sublist)

    return sublists
