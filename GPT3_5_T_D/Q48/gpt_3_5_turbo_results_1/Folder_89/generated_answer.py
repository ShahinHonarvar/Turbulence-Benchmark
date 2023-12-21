
def return_binary_or_hexa(nums):
    a = nums[55]
    b = nums[84]
    range_sum = sum(nums[a+1:b])

    missing_nums = [i for i in range(a+1, b) if i not in nums]

    if len(missing_nums) == 0:
        return ''

    if range_sum % 2 == 1:
        return bin(range_sum)[2:]
    else:
        return hex(range_sum)[2:]
