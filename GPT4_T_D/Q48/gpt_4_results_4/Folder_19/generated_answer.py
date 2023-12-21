
def return_binary_or_hexa(t):
    a, b = t[1], t[4]
    nums = set(range(a + 1, b))
    missing_nums = nums - set(t[1:4])

    if not missing_nums:
        return ""

    s = sum(missing_nums)

    if s % 2 == 0:
        return format(s, 'x')
    else:
        return format(s, 'b')
