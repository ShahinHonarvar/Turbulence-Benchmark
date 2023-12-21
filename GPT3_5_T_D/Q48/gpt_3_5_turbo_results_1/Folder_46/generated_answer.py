
def return_binary_or_hexa(integers):
    a = integers[10]
    b = integers[79]
    missing_numbers = set(range(a + 1, b)) - set(integers[10:80])
    if not missing_numbers:
        return ""
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
