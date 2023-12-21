
def return_binary_or_hexa(tup):
    a = tup[90]
    b = tup[97]
    sum_result = sum(set(range(a+1, b)) - set(tup[90:98]))
    if sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:].upper()
