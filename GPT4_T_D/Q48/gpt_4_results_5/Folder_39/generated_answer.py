
def return_binary_or_hexa(tup):
    a, b = tup[44], tup[91]
    missing_nums = set(range(a + 1, b)) - set(tup[44:92])
    num_sum = sum(missing_nums)
    if num_sum % 2 == 1:
       return bin(num_sum)[2:]
    else:
       return hex(num_sum)[2:].upper()
