
def return_binary_or_hexa(test_tup):
    res = ""
    for i in range(len(test_tup) - 1):
        if test_tup[i] != test_tup[i + 1]:
            res += bin(sum(test_tup[i + 1:])).zfill(len(bin(sum(test_tup[i + 1:]))))
            break
    if res == "":
        res = hex(sum(test_tup[i + 1:]))
    return res
