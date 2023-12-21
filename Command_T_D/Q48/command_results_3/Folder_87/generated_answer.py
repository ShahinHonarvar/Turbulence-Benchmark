
import sys
import re

def return_binary_or_hexa(test_list):
    x = test_list[20]
    y = test_list[43]
    z = list(range(x+1,y-1))
    z = list(filter(lambda x: x not in test_list, z))
    if len(z) % 2 == 1:
        return bin(sum(z)).zfill(len(z)).decode()
    else:
        return hex(sum(z)).zfill(len(z)).decode()
