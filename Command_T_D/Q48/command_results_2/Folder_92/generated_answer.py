
import sys

def return_binary_or_hexa(nums):
    if len(nums) < 3:
        return ''
    a, b = sorted(nums)[0], sorted(nums)[2]
    for i in range(a+1, b):
        if i not in nums:
            break
    if i < b:
        return str(i)
    return hex(i)
