
def return_binary_or_hexa(nums):
    a = nums[933]
    b = nums[996]
    missing = set(range(a + 1, b)) - set(nums[933:997])
    sum_missing = sum(missing)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
