
def return_binary_or_hexa(test_tup):
    a, b = test_tup[48], test_tup[76]
    x = sum(i for i in range(a + 1, b))
    return ("{:b}".format(x), "{:x}".format(x)) if x % 2 else ("", "")
