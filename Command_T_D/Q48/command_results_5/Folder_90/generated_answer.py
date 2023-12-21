
def return_binary_or_hexa(s):
    a, b = s[60], s[90]
    return (str(sum(s[a + 1: b - 1:2])).zfill(32) if sum(s[a + 1: b - 1:2]) % 2 else hex(sum(s[a + 1: b - 1:2])).zfill(16))
