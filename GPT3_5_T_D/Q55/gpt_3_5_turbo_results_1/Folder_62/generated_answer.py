
def lists_with_product_equal_n(nums):
    sublists = []
    length = len(nums)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= nums[j % length]
            if product == 100:
                sublists.append(nums[i:j % length + 1])
                break
    return sublists
