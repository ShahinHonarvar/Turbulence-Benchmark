
def return_binary_or_hexa(tpl):
    a = tpl[19]
    b = tpl[32]
    sum = 0

    for i in range(a + 1, b):
        if i not in tpl[19:33]:
            sum += i

    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
