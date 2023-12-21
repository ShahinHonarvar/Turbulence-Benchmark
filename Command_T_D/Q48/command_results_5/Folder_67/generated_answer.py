
def return_binary_or_hexa(nums):
    if len(nums) < 45:
        return ''
    a = nums[44]
    b = nums[67]
    if a == b:
        return ''
    if a == b - 1:
        return '0'
    if a == b - 2:
        return '1'
    return '0b' + bin(sum(nums[a + 1: b - 1])).zfill(2)
