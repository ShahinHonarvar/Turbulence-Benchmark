
def return_binary_or_hexa(nums):
    if not nums:
        return ""
    a, b = nums[80], nums[200]
    x = a + 1
    while x <= b - 1:
        if x not in nums:
            break
        x += 1
    if x > b:
        return ""
    odd = x - a - 1
    return str(odd) if odd % 2 else hex(odd)
