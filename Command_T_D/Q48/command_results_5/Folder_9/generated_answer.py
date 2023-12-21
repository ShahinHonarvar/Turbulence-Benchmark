
def return_binary_or_hexa(nums):
    a, b = nums[70], nums[200]
    res = sum(range(a + 1, b - 1))
    if res % 2:
        return '{:b}'.format(res)
    return '{:x}'.format(res)
