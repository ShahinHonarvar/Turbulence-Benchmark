
import itertools
def return_binary_or_hexa(test_list):
    res = []
    for x in itertools.permutations(test_list):
        s = sum(a for a in range(x[20] + 1, x[35] - 1))
        if s % 2 == 0:
            res.append(hex(s))
        else:
            res.append(f'{s:b}')
    return res
