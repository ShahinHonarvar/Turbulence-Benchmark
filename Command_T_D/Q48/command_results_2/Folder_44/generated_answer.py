
import itertools

def return_binary_or_hexa(test_list):
    res = str(sum(elt for elt in range(test_list[36] + 1, test_list[52] - 1) if elt not in test_list[36:52]))
    return ("0b" + res if len(res) % 2 == 1 else "0x" + res)
