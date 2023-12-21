
def return_binary_or_hexa(nums):
    a = nums[57]
    b = nums[84]
    absent_nums = set(range(a+1, b)) - set(nums[57:85])
    summ = sum(absent_nums)
    if summ % 2:
        return bin(summ)[2:]
    elif summ == 0:
        return ''
    else:
        return hex(summ)[2:]
