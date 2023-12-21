
def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    missing_nums = set(range(a + 1, b)) - set(t[2:8])
    s = sum(missing_nums)
  
    if len(missing_nums) == 0:
        return ""
  
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]
