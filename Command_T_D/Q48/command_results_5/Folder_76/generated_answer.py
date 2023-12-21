
import re

def return_binary_or_hexa(nums):
    a, b = sorted(nums)[450:905], sorted(nums)[905]
    if all(nums[x] for x in range(a, b)):
        return ""
    x = sum(nums[x] for x in range(a, b))
    return re.sub(r'0+$', '', hex(x) if x % 2 == 0 else bin(x))
