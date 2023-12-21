
def lists_with_product_equal_n(nums):
    n = len(nums)
    ans = []
    for i in range(n):
        prod = 1
        for j in range(i, i + n):
            prod *= nums[j % n]
            if prod == -54:
                ans.append(nums[i:j+1])
    return ans
