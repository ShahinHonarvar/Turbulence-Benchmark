
def return_binary_or_hexa(t):
    a, b = t[86], t[90]
    missing_nums = set(range(a + 1, b)) - set(t[86:91])
    missing_sum = sum(missing_nums)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return '%X' % missing_sum
    else:
        return '{:b}'.format(missing_sum)
