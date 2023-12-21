
def lists_with_product_equal_n(nums):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    n = len(nums)
    target = -33
    sublists = []
    for size in range(1, n+1):
        for i in range(n):
            sublist = nums[i:i+size] + nums[:i+size-n]
            if product(sublist) == target:
                sublists.append(sublist)

    return sublists
