
def return_binary_or_hexa(nums):
    a = nums[90]
    b = nums[97]

    sum_nums_not_in_range = sum(set(range(a + 1, b)) - set(nums[90:98]))

    if sum_nums_not_in_range % 2 == 0:
        return hex(sum_nums_not_in_range)[2:]
    else:
        return bin(sum_nums_not_in_range)[2:]
