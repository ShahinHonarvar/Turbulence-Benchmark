
def return_binary_or_hexa(t):
    a = t[44]
    b = t[67]
    nums = set(t)
    total = 0
    for i in range(a + 1, b):
        if i not in nums:
            total += i
    if total == 0:
        return ""
    elif total % 2 == 0:
        return format(total, 'X')
    else:
        return format(total, 'b')
