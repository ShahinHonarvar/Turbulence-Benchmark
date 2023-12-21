
import sys

def return_binary_or_hexa(test_list):
    a, b = test_list[32], test_list[99]
    if b - a == 1:
        return ""
    if (a + 1) + (b - a - 1) % 2 == 0:
        return hex(a + 1 + b - a - 1)
    else:
        return "0b" + bin(a + 1 + b - a - 1)
