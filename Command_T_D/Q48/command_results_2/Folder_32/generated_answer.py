
def return_binary_or_hexa(tup):
    i = 86
    j = 90
    odd = True
    while i < j:
        if tup[i] == tup[j]:
            j -= 1
        elif tup[i] < tup[j]:
            odd = False
        else:
            i += 1
    return ("" if odd else hex(sum(range(tup[i] + 1, tup[j] - 1))))
