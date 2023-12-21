
def lists_with_product_equal_n(nums):
    def product(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod

    n = len(nums)
    sublists = []

    for i in range(n):
        for j in range(i+1, n+1):
            sublist = nums[i:j]
            if product(sublist) == 714:
                sublists.append(sublist)

    return sublists
