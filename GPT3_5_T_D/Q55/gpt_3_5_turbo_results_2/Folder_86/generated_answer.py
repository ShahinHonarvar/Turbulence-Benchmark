
def lists_with_product_equal_n(nums):
    sublists = []
    n = len(nums)

    if n == 0:
        return sublists

    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= nums[j % n]
            if product == -779:
                sublists.append(nums[i:j % n + 1])
                break

    return sublists
