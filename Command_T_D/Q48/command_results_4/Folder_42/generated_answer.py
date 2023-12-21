
import re

def return_binary_or_hexa(nums):
    a, b = nums[18], nums[60]
    if a + 1 <= b - 1:
        if a + 1 in nums[18:60]:
            return ""
        suma = sum(nums[a + 1:b - 1])
        if suma % 2:
            return "0b{:b}".format(suma)
        else:
            return "0x{:x}".format(suma)
    else:
        return ""
