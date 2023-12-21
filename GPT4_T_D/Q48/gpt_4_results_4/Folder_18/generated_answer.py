
def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[90]
    nums_in_range = set(nums[56:90])

    total = sum([i for i in range(a + 1, b) if i not in nums_in_range])
    if total == 0:
        return ''
    elif total % 2 == 0:
        return str(hex(total))[2:]
    else:
        return str(bin(total))[2:]
