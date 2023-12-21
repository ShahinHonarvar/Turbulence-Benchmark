
def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]
    sum_absent = sum(set(range(a + 1, b)) - set(numbers[69:98]))
    if sum_absent % 2:
        return bin(sum_absent)[2:]
    else:
        return hex(sum_absent)[2:].upper() if sum_absent != 0 else ""
