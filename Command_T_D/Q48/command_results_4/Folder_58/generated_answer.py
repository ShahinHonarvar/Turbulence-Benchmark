
import operator as op

def return_binary_or_hexa(test_tup):
    res = test_tup[871] - test_tup[275]
    if res % 2:
        return bin(res).zfill(len(bin(res))).decode()
    else:
        return hex(res).zfill(len(hex(res))).decode()
