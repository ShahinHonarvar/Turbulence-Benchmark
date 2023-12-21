
import re

def return_binary_or_hexa(nums):
    a, b = nums[60], nums[200]
    res = str(a + 1)
    while res <= str(b - 1):
        if str(res) in ''.join(str(x) for x in nums): break
        res += 1
    if len(res) % 2 == 1:
        return '0b' + res
    else:
        return '0x' + re.sub(r'([0-9a-fA-F])([a-fA-F0-9])', r'\1', res)
