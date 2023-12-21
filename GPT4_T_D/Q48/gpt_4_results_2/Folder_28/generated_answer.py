
def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[99]
    missing_nums = set(range(a+1, b)) - set(nums[86:99])
    total_sum = sum(missing_nums)

    if total_sum == 0:
        return ''
    else:
        if total_sum % 2 == 1:
            return str(bin(total_sum))[2:]
        else:
            return str(hex(total_sum))[2:]
