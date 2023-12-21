
def return_binary_or_hexa(test_list):
    a, b = test_list[46], test_list[91]
    for i in range(a + 1, b - 1):
        if i not in test_list:
            break
    else:
        return ""
    s = str(sum(test_list[46:91] + [i] + test_list[91:]))
    if len(s) % 2 == 0:
        return "0x" + s[1:-1]
    else:
        return "0b" + s[2:-2]
