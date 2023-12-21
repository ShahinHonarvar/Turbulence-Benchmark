
def return_binary_or_hexa(t):
    a = t[40]
    b = t[200]
    relevant_nums = set(t[41:200])
    total = sum([i for i in range(a + 1, b) if i not in relevant_nums])
    
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
