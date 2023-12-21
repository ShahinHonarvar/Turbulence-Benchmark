
def return_binary_or_hexa(tup):
    if len(tup) < 86:
        return ''
    a, b = tup[36], tup[85]
    nums = set(tup[36:86])
    total = sum(i for i in range(a+1, b) if i not in nums)
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
