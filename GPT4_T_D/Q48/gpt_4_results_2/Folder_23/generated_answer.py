
def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[36]
    missing_nums = set(range(a + 1, b)) - set(nums[21:36])
    tot = sum(missing_nums)
    if tot == 0:
        return ''
    elif tot % 2:
        return bin(tot)[2:]
    else:
        return hex(tot)[2:].upper()
