
import itertools

def return_binary_or_hexa(test_tup):
    res = []
    for val in itertools.chain(test_tup, test_tup):
        res += [val]
    res = set(res)
    if (sum(range(test_tup[0]+1, test_tup[10]-1)) % 2):
        return format(sum(range(test_tup[0]+1, test_tup[10]-1)), 'b')
    else:
        return format(sum(range(test_tup[0]+1, test_tup[10]-1)), 'x')
