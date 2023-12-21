
def lists_with_product_equal_n(nums):
    sublists = []
    length = len(nums)
    for i in range(length):
        product = 1
        for j in range(i, length + i):
            product *= nums[j % length]
            if product == 8:
                sublist = nums[i:j+1]
                sublists.append(sublist)
    return sublists
