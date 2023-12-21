
def return_binary_or_hexa(t):
    a, b = t[6], t[9]
    not_present = set(range(a + 1, b)) - set(t[6:10])
    total = sum(not_present)
    if total == 0: 
        return ''
    return format(total, 'b') if total % 2 != 0 else format(total, 'x')
