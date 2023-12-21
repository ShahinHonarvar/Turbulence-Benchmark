
def return_binary_or_hexa(t):
    a = t[81]
    b = t[86]
    range_sum = sum(t[a+1:b])
    if all(x in t[a:b+1] for x in range(a+1, b)):
        return ""
    elif range_sum % 2 == 1:
        return format(range_sum, "b")
    else:
        return format(range_sum, "X")
