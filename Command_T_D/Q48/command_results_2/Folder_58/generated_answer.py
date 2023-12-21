
def return_binary_or_hexa(tup):
    a, b = tup[275], tup[871]
    x = a + 1
    y = b - 1
    return (str(sum(tup[x:y + 1]) + 1) + "0b")[0] if sum(tup[x:y + 1]) % 2 else str(sum(tup[x:y + 1]) + 1) + "0x"
