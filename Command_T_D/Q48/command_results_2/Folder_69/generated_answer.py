
import sys

def return_binary_or_hexa(test_list):
    odd = 0
    even = 0
    res = ""
    for i in range(len(test_list)-1):
        if i == 39:
            odd += 1
        elif i == 43:
            even += 1
        else:
            odd += test_list[i]
            even += test_list[i]
        if odd % 2 == 1:
            res += str(odd)
            break
        elif even % 2 == 1:
            res += hex(odd)
            break
        else:
            res += hex(odd)
            break
    return res
