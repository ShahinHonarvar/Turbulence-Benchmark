
def return_binary_or_hexa(t):
    a = t[43]
    b = t[70]
    num_list = set(t[44:70])
    sum = 0
    for i in range(a + 1, b):
        if i not in num_list:
            sum += i
    
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
