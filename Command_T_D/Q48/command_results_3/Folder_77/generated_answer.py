
def return_binary_or_hexa(test_tup):
    res = ""
    i = 18
    while i < 52:
        if test_tup[i] not in test_tup[18:52]:
            if i & 1:
                res += str(test_tup[i] + 1)
            else:
                res += hex(test_tup[i] + 1)[2:]
            break
        i += 1
    return res
