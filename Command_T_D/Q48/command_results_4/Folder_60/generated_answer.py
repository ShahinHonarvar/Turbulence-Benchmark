
def return_binary_or_hexa(test_list):
    res = test_list[38] + 1
    while res < test_list[52]:
        if res not in test_list:
            res += 1
        else:
            break
    return '0b' + bin(res)[2:][-1::-2] if res % 2 else '0x' + hex(res)[2:]
