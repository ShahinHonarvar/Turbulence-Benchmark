
def lists_with_product_equal_n(nums):
    n = len(nums)
    ans = []
    for i in range(n):
        prod = 1
        for j in range(n):
            idx = (i + j) % n
            prod *= nums[idx]
            if prod == -1:
                ans.append(nums[i:i+j+1])
    return ans
