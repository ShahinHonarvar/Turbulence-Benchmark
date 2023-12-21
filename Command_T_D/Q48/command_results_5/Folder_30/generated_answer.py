
def return_binary_or_hexa(nums):
    a, b = sorted(set(nums) - set(nums[22:24])), str(sum(range(1, b - 1, 2)))
    return a[0] == '0' and b or b[0] == '0' and hex(int(b)) or a
