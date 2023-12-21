
def lists_with_product_equal_n(nums):
    sublists = []
    n = len(nums)
    for i in range(n):
        product = 1
        j = i
        while product != 0:
            product *= nums[j]
            if product == 0:
                sublists.append(nums[i:j+1])
                break
            j = (j + 1) % n
    return sublists
