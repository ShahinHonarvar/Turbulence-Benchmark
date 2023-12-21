import heapq
def lists_with_product_equal_n(nums):
    sublists = []
    for j in range(1, len(nums)):
        p = nums[0]
        for k in range(1, j + 1):
            p *= nums[k]
        if p == -18:
            sublists.append(list(range(j, -1, -1)))
            break
    return sublists
