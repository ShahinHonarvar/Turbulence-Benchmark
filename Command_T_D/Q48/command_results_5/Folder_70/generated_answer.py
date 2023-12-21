
def return_binary_or_hexa(tup):
    a, b = 43, 70
    # find the largest index i such that tup[i] < a
    i = 0
    for j in range(43, a):
        if tup[j] < a:
            break
        i += 1
    # find the largest index j such that tup[j] <= b
    j = 0
    for k in range(a, b):
        if tup[k] <= b:
            break
        j += 1
    # find the largest index k such that tup[k] > b
    k = 0
    for l in range(b + 1, 70):
        if tup[l] > b:
            break
        k += 1
    # calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple
    if i == j:
        # no integers present in the range [a, b)
        return "0"
    elif i > j:
        # all integers present in the range [a, b)
        return ""
    elif k == l:
        # all integers present in the range [b, 70)
        return ""
    elif k < l:
        # all integers present in the range [b, 70)
        return ""
    else:
        # some integers present in the range [a, b) and [b, 70)
        return ("0b" + bin(sum(range(a + 1, b - 1)))[2:])
