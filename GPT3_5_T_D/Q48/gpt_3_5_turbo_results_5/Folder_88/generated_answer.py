
def return_binary_or_hexa(t: tuple) -> str:
    a = t[3]
    b = t[9]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in t[3:9]:
            total_sum += i
            
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
