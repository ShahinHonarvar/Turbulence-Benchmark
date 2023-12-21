
def lists_with_product_equal_n(nums):
    def product(nums):
        result = 1
        for num in nums:
            result *= num
        return result

    sublists = []
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length+1):
            sublist = nums[i:j]
            if product(sublist) == -72:
                sublists.append(sublist)
    return sublists
