
def return_binary_or_hexa(nums):
    a = nums[19]
    b = nums[32]
    missed = set(range(a+1, b)) - set(nums[19:33])
    sum_missed = sum(missed)
    if sum_missed:
        if sum_missed % 2 == 1:
            return bin(sum_missed)[2:]
        else:
            return hex(sum_missed)[2:].upper()
    else:
        return ""
