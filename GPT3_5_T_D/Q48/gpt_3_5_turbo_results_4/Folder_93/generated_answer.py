
def return_binary_or_hexa(nums):
    a = nums[57]
    b = nums[85]

    total_sum = 0
    missing_nums = []
    for num in nums[a+1:b]:
        if num not in nums[57:85]:
            total_sum += num
        else:
            missing_nums.append(num)

    if missing_nums == []:
        return ""

    if total_sum % 2 == 1:
        return format(total_sum, "b")
    else:
        return format(total_sum, "x")
