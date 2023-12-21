
import itertools

def return_binary_or_hexa(test_tup):
    res = list(map(str, itertools.chain(
        itertools.permutations(test_tup),
        itertools.permutations(test_tup[1:]),
    )))
    res = list(res[1:]) + res[0]
    return '0b' + res if len(res) % 2 == 1 else '0x' + res
