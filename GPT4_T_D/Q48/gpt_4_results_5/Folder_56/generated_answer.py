
def return_binary_or_hexa(nums):
    a, subset, b = nums[7], nums[7:10], nums[9]

    missing = [i for i in range(a + 1, b) if i not in subset]

    sum_missing = sum(missing)

    if sum_missing == 0:
        return ""
    elif sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
