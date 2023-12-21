
def return_binary_or_hexa(nums):
    a, b = nums[0] + 1, nums[9] - 1
    missing_numbers_sum = sum(set(range(a, b+1)) - set(nums))

    if missing_numbers_sum % 2 == 0:
        return hex(missing_numbers_sum)[2:]
    else:
        return bin(missing_numbers_sum)[2:]
