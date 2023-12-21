
def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[4]
    missing_nums = [num for num in range(a + 1, b) if num not in nums[1:4]]
    if len(missing_nums) == 0:
        return ""
    else:
        sum_missing_nums = sum(missing_nums)
        if sum_missing_nums % 2 == 1:
            return bin(sum_missing_nums)[2:]
        else:
            return hex(sum_missing_nums)[2:]
