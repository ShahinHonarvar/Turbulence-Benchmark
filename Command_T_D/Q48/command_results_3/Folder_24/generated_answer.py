
import binary
import hexadecimal

def return_binary_or_hexa(test_list):
    for i in range(test_list[13] + 1, test_list[91] - 1):
        if i not in test_list:
            break
    else:
        return ""
    if test_list[13] + 1 == test_list[91] - 1:
        return ""
    if test_list[13] % 2 == test_list[91] % 2:
        return binary.to_binary(test_list[13] + 1, test_list[91] - 1)
    else:
        return hexadecimal.to_hexadecimal(test_list[13] + 1, test_list[91] - 1)
