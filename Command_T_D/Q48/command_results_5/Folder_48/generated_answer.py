
import itertools

def return_binary_or_hexa(tup):
    for x in itertools.combinations(tup):
        if x[0] + 1 <= x[1] - 1:
            break
    else:
        return ""
    return ("{:b}".format(sum(set(range(x[0] + 1, x[1] - 1)))),
