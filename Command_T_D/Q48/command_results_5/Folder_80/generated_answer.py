
def return_binary_or_hexa(test_tup):
    res = ""
    a, b = test_tup[57], test_tup[84]
    res += sum(x for x in range(a + 1, b - 1))
    if res % 2:
        res = f"0{res}"
    else:
        res = f"{res:x}"
    return res
