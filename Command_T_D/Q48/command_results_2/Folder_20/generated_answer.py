
import re
def return_binary_or_hexa(test_list):
    res = str(sum(i for i in range(test_list[27] + 1, test_list[96] - 1, 2) if i not in test_list))
    if res[0] == '0':
        return '0x' + res[1:]
    else:
        return '0b' + re.sub(r'([01]+)0', r'\1', res)
