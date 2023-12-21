
def return_binary_or_hexa(nums):
    a, b = nums[69], nums[97]
    s = str(sum(nums[69] + 1:nums[97] - 1))
    if len(s) % 2 == 1:
        return f'{s}'
    else:
        return f'0x{s}'
