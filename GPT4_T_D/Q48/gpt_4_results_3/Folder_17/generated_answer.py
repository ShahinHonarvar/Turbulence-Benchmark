
def return_binary_or_hexa(nums):
    a = nums[73]
    b = nums[84]
    sum_ = sum(set(range(a + 1, b)) - set(nums[73:85]))
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()
