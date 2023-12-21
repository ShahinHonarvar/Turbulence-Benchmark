
def return_binary_or_hexa(test_list):
    res = str(sum(range(test_list[0] + 1, test_list[8] - 1, 2)))
    if len(res) == 1:
        return ""
    elif len(res) == 2:
        return "0b" + res[1:]
    else:
        return "0x" + res[2:]
