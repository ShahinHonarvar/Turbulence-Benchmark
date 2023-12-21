
import itertools

def return_binary_or_hexa(test_tup):
    for idx in range(25, 80):
        if idx not in test_tup:
            break
    else:
        return ''
    for idx in range(a+1, b-1):
        if idx not in test_tup:
            break
    else:
        return ''
    val = sum(list(itertools.takewhile(lambda x: x not in test_tup, range(a+1, b-1))))
    return ('0b' + bin(val)[2:][-2:-1] if val % 2 else hex(val)[2:][-2:-1])
