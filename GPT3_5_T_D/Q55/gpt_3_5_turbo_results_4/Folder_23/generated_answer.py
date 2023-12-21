
def lists_with_product_equal_n(nums):
    def product(nums):
        p = 1
        for num in nums:
            p *= num
        return p

    sublists = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            sublist = nums[i:j]
            if product(sublist) == -95:
                sublists.append(sublist)
    return sublists
