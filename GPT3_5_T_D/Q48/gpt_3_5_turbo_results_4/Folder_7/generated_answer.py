
def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[97]

    missing_nums = [x for x in range(a + 1, b) if x not in nums[10:98]]

    if len(missing_nums) == 0:
        return ""

    total = sum(missing_nums)

    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
