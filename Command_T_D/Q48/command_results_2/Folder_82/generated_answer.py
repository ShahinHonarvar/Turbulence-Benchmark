
def return_binary_or_hexa(test_tup):
    a, b = test_tup[20], test_tup[200]
    if (a + 1) > (b - 1):
        return ""
    x = a + 1
    y = b - 1
    flag = 1
    while x <= y:
        if test_tup[x] == test_tup[y]:
            break
        else:
            if flag == 1:
                test_tup[x] = 1
            else:
                test_tup[y] = 1
            flag = 0
        x += 1
        y -= 1
    if flag == 1:
        return "0b{:b}".format(sum(test_tup[a + 1:b]))
    else:
        return "0x{:x}".format(sum(test_tup[a + 1:b]))
