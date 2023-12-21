
def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[7]
    missing_nums = [i for i in range(a+1, b) if i not in nums[2:7]]
    if not missing_nums:
        return ""
    sum_of_missing_nums = sum(missing_nums)
    if sum_of_missing_nums % 2 == 0:
        return hex(sum_of_missing_nums)[2:].upper()
    else:
        return bin(sum_of_missing_nums)[2:]
