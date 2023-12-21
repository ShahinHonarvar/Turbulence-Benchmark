
def return_binary_or_hexa(t):
    a = t[7]
    b = t[9]
    absent_nums = set(range(a+1, b)) - set(t[7:10])
    num_sum = sum(absent_nums)
    if num_sum == 0:
        return ''
    if num_sum % 2 == 0:
        return hex(num_sum)[2:]
    else:
        return bin(num_sum)[2:]
