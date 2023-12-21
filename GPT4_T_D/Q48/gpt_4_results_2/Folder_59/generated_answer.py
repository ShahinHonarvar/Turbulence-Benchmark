
def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[10]
    sum_ = sum(set(range(a + 1, b)) - set(nums[1:11]))
    if sum_ % 2 == 0:
        return hex(sum_)[2:].upper()
    else:
        return bin(sum_)[2:]
