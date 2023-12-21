
def return_binary_or_hexa(numbers):
    a = numbers[16]
    b = numbers[87]
    missing_nums = set(range(a + 1, b)) - set(numbers[16:88])
    total_sum = sum(missing_nums)
    if total_sum == 0:
        return ""
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]
