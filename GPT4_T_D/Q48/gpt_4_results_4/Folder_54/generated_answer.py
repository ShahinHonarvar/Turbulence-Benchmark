
def return_binary_or_hexa(nums):
    a = nums[35]
    b = nums[64]

    missed_nums = set(range(a + 1, b)) - set(nums[35:65])
    total_sum = sum(missed_nums)

    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
