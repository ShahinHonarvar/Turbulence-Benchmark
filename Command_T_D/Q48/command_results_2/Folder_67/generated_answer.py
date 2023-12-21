
def return_binary_or_hexa(test_tup):
    lst = list(test_tup)
    a = lst[44]
    b = lst[67]
    s = a + 1
    e = b - 1
    if s <= e:
        s += 1
        e += 1
        lst[a] += s - a
        lst[b] += e - b
        lst[a] %= 2
        lst[b] %= 2
        if lst[a] != 0:
            return f"0{lst[a]:b}"
        elif lst[b] != 0:
            return f"0{lst[b]:x}"
        else:
            return ""
    else:
        return ""
