
def return_binary_or_hexa(test_list):
    a, b = test_list[77], test_list[84]
    s = sum(i for i in range(a + 1, b - 1) if i not in test_list[77:84])
    return ("{:b}".format(s) if s % 2 else "{:x}".format(s))
