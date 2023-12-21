
def return_binary_or_hexa(t):
    a = t[36]
    b = t[85]
    integers_between_a_and_b = set(t[37:85])
    sum = 0
    for i in range(a+1, b):
        if i not in integers_between_a_and_b:
            sum += i
    if sum == 0:
        return ""
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
