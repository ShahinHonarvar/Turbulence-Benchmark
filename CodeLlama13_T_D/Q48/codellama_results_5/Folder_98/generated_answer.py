
def return_binary_or_hexa(tup):
    a, b = tup[6], tup[7]
    sum_odd = 0
    for i in range(a+1, b-1):
        if i not in tup:
            sum_odd += 1
    if sum_odd % 2 == 0:
        return hex(sum_odd)[2:]
    else:
        return bin(sum_odd)[2:]
