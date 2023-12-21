
def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums*2
    res = []
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            if(j - i == n):
                break
            sublist = nums[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -5:
                res.append(sublist)
    return res
