
def return_binary_or_hexadecimal(tup):
    a = tup[60] + 1
    b = tup[200] - 1
    s = sum(i for i in range(a, b+1) if i not in tup)
    return bin(s)[2:] if s % 2 else hex(s).upper()[2:]
