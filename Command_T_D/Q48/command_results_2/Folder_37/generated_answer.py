
def return_binary_or_hexa(s):
    a, b = sorted(set(s))
    return ("".join(str(i) for i in range(a + 1, b)) + "b" if a % 2 == 1 and len(str(a + 1)) == len(str(b - 1)) else hex(a + 1) if a % 2 == 1 else hex(b - 1))
