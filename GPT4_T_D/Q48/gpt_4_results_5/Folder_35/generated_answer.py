
def return_binary_or_hexa(nums):
    a, b, vals = nums[77], nums[84], set(nums[77:85])
    total = sum(set(range(a+1, b)) - vals)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
