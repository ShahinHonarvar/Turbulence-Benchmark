
def return_binary_or_hexa(nums):
    a, b = nums[2], nums[8]
    s = str(sum(nums[3:5] + nums[6:8]))
    if s[0] == '0':
        s = '0' + s[1:]
    if s[0] == 'x':
        s = '0x' + s[1:]
    if len(s) == 1:
        s = '0' + s
    return s
