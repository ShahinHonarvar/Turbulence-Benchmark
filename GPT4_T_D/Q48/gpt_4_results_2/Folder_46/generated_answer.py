
def return_binary_or_hexa(raw_tuple):
    a = raw_tuple[10]
    b = raw_tuple[79]
    missing_nums = [i for i in range(a + 1, b) if i not in raw_tuple[10:80]]
    num_sum = sum(missing_nums)
    if num_sum == 0:
        return ''
    elif num_sum % 2 == 0:
        return hex(num_sum)[2:]
    else:
        return bin(num_sum)[2:]
