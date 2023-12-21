
def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[97]
    sum_val = sum(set(range(a + 1, b)) - set(numbers[90:98]))
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()
