
import itertools

def return_binary_or_hexa(test_list):
    for start, end in itertools.permutations(test_list, 2):
        if start != end:
            # binary
            if start <= 60 and end >= 90:
                return '0b' + bin(sum(list(range(start + 1, end - 1, 2)))).zfill(64)
            # hex
            if start <= 60 and end >= 90:
                return '0x' + hex(sum(list(range(start + 1, end - 1, 2)))).zfill(16)
    return ''
