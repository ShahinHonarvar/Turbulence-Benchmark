
def return_binary_or_hexa(test_tup):
    res = test_tup[110] + 1
    while True:
        if res in test_tup[110:348]:
            break
        elif res % 2 == 1:
            return '0b' + bin(res).zfill(8).decode("ascii")
        else:
            return '0x' + hex(res).zfill(4).decode("ascii")
