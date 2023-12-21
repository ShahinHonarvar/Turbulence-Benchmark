
def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[93]
    sum_val = sum(set(range(a + 1, b)) - set(nums[20:94]))
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()
