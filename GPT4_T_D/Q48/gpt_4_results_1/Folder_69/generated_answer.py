
def return_binary_or_hexa(t):
    a, b = t[39], t[43]
    all_nums = set(range(a + 1, b))
    nums_in_t = set(t[39:44])
    nums_not_in_t = all_nums.difference(nums_in_t)
    s = sum(nums_not_in_t)
    if s == 0:
        return ''
    elif s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]
