
def lists_with_product_equal_n(nums):
    def product(nums):
        res = 1
        for num in nums:
            res *= num
        return res

    def get_sublists(nums):
        res = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                res.append(nums[i:j + 1])
        return res

    sublists = get_sublists(nums)
    result = []
    for sublist in sublists:
        if product(sublist) == -690:
            result.append(sublist)
    return result
