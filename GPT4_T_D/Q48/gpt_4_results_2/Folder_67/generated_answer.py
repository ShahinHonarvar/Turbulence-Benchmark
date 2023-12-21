
def return_binary_or_hexa(t):
    a, b = t[44], t[67]
    nums = set(t[44:68])
    total = sum(set(range(a + 1, b)).difference(nums))
    if total == 0:
        return ""
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
