
import sys

sys.setrecursionlimit(10**6)


def return_binary_or_hexa(test_tup):
    a, b = test_tup[38], test_tup[81]
    return_str = ""
    try:
        return_str = str(sum(range(a + 1, b - 1)))
        if len(return_str) % 2 == 1:
            return_str = return_str.zfill(len(return_str))
        else:
            return_str = hex(int(return_str))
    except:
        pass
    return return_str
