 
def lists_with_product_equal_n(nums):
    res = []
    curr = 0
    for i in range(len(nums)):
        curr = curr * nums[i] % 851
        if curr == 0:
            break
        res += [[nums[i]]
    return res
