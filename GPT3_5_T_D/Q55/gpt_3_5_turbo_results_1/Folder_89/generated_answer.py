
def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums) + i):
            index = j % len(nums)
            product *= nums[index]
            if product == 57:
                sublists.append(nums[i:index+1])
    return sublists
