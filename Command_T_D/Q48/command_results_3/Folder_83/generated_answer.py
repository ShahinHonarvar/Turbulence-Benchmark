
import re

def return_binary_or_hexa(nums):
    a, b = nums[90], nums[200]
    if a < b:
        return (
            f'{sum(range(a+1, b-1))}'
            if sum(range(a+1, b-1)) % 2 == 0
            else f'{sum(range(a+1, b-1))}b'
        )
    return ''
