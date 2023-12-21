
import bin
import hex

def return_binary_or_hexa(test_tup):
    res = 0
    for idx in range(test_tup[44], test_tup[78]+1):
        if idx not in test_tup:
            res += idx
    if res % 2 == 1:
        return bin(res).zfill(len(bin(res))).decode('utf-8')
    return hex(res).zfill(len(hex(res))).decode('utf-8')
