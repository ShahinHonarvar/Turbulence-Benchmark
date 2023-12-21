
def return_binary_or_hexa(nums):
    a, b = nums[3], nums[8]
    missing_nums_sum = sum(i for i in range(a + 1, b) if i not in nums[3:9])
    if missing_nums_sum == 0:
        return ''
    elif missing_nums_sum % 2 == 0:
        return hex(missing_nums_sum)[2:].upper()
    else:
        return bin(missing_nums_sum)[2:]
