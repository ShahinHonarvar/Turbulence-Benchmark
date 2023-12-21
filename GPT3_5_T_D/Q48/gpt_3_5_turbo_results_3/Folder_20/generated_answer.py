
def return_binary_or_hexa(nums):
    a = nums[27]
    b = nums[96]

    missing_nums = set(range(a + 1, b)) - set(nums[27:97])
    if len(missing_nums) == 0:
        return ""

    sum = 0
    for num in missing_nums:
        sum += num

    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
