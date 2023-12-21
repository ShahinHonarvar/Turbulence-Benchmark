
import itertools

def return_binary_or_hexa(nums):
    res = sum(n for n in range(nums[2]+1, nums[5]-1))
    if res % 2:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
