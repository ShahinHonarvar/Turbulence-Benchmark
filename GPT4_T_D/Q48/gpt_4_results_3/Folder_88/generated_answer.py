
def return_binary_or_hexa(tuple):
    a = tuple[3]
    b = tuple[9]
    nums = set(tuple[4:9])
    sum = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()
