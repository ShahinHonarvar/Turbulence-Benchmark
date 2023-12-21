
def return_binary_or_hexa(nums):
    a = nums[69]
    b = nums[97]
    missing_nums = set(range(a + 1, b)) - set(nums[70:97])
    if missing_nums:
        total_sum = sum(missing_nums)
        if total_sum % 2 == 1:
            return bin(total_sum)[2:]
        else:
            return hex(total_sum)[2:]
    else:
        return ''
