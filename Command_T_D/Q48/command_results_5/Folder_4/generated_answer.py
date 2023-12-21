
def return_binary_or_hexa(test_list):
    a, b = test_list[49], test_list[74]
    lst = list(range(a + 1, b - 1))
    if set(lst) & set(test_list[49:74]):
        return ""
    odd = sum(x for x in lst if x % 2 == 1)
    if odd <= 9:
        return "0b{:b}".format(odd)
    else:
        return "{:x}".format(odd)
