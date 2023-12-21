
def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[8]

    missing_nums = [num for num in range(a + 1, b) if num not in nums[1:9]]
    total = sum(missing_nums)

    if total % 2 != 0:
        return format(total, 'b')
    else:
        return format(total, 'x') if total != 0 else ""
