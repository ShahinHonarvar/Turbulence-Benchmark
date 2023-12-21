
import sys

def return_binary_or_hexa(nums):
    a, b = sorted(nums)[44], sorted(nums)[91]
    if a == b:
        return ''
    if a % 2 == b % 2:
        return '0b' + bin(a + b - 1).count('1').zfill(len(bin(a + b - 1)) - 2)
    else:
        return '0x' + hex(a + b - 1)[2:]
