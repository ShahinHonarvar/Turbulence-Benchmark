
def return_binary_or_hexa(nums):
    s = str(nums[0] + 1)
    if s[-1] == '1':
        s += '0'
    if s[-1] == '2':
        s += '4'
    s += str(nums[-1] - 1)
    return s
