
import itertools

def return_binary_or_hexa(test_list):
    num_list = list(itertools.range(test_list[18] + 1, test_list[52] - 1))
    if set(num_list) & set(test_list[18:52]):
        return ""
    if len(str(sum(num_list))) % 2 == 1:
        return "0b" + str(sum(num_list))
    return "0x" + hex(sum(num_list))
