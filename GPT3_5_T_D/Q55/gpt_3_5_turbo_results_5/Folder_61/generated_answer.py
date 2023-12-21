
def lists_with_product_equal_n(nums):
    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result

    n = len(nums)
    target = -10
    sublists = []
    for i in range(n):
        for j in range(i, n):
            sublist = nums[i:j+1]
            if product(sublist) == target:
                sublists.append(sublist)
    return sublists
