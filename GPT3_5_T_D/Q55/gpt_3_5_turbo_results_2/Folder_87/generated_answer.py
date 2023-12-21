
def lists_with_product_equal_n(nums):
    sublists = []
    n = len(nums)
    product = 1
    start = 0

    for i in range(n + 1):
        while product > 27 and start < i - 1:
            product //= nums[start]
            start += 1

        if product == 27:
            sublists.append(nums[start:i])

        if i < n:
            product *= nums[i]

    return sublists
