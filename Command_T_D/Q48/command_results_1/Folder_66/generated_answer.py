
import sys

def return_binary_or_hexa(test_list):
    for i in range(10):
        if test_list[i] == test_list[11]:
            continue
        elif test_list[i] == test_list[76]:
            break
        else:
            return ("0b" + bin(test_list[i + 1]).count("1").zfill(8))
    else:
        return ("0x" + hex(test_list[12]).upper().zfill(8))
