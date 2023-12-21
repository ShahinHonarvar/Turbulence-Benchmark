
def return_binary_or_hexa(nums):
    a, b = nums[933], nums[996]
    res = sum(nums[a + 1 : b])
    if res % 2:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
