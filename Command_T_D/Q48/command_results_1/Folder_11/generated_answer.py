
def return_binary_or_hexa(test_list):
    res = test_list[48] + 1
    while res <= test_list[76]:
        if res not in test_list:
            res += 1
        else:
            break
    return ("0b" + bin(res - 1)[2:]).zfill(res - 1) if res - 1 % 2 else hex(res - 1)[2:]
