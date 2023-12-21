
def lists_with_product_equal_n(nums):
    res = []
    len_nums = len(nums)
    nums += nums
    for i in range(len_nums):
        for j in range(i+1, len_nums + i + 1):
            product = 1
            for num in nums[i:j]:
                product *= num
            if product == 46:
                res.append(nums[i:j])
    return res
