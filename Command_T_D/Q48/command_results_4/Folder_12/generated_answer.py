
def return_binary_or_hexa(nums):
    a, b = nums[16], nums[87]
    if not (a + 1 <= b - 1):
        return ""
    odd = b - a - 1
    if odd % 2:
        return format(odd, 'b')
    return format(odd, 'x')
