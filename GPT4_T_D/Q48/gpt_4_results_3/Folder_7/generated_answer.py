
def return_binary_or_hexa(int_tuple):
    a = int_tuple[10]
    b = int_tuple[97]
    missing_nums = set(range(a + 1, b)) - set(int_tuple[10:98])
    num_sum = sum(missing_nums)
    if num_sum == 0:
        return ''
    elif num_sum % 2 == 0:
        return hex(num_sum)[2:]
    else:
        return bin(num_sum)[2:]
