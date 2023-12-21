
def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[12]
    missing_nums = set(range(a+1, b)) - set(nums[10:13])
    sum_missing = sum(missing_nums)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing).replace('0b', '')
    else:
        return hex(sum_missing).replace('0x', '').upper()
