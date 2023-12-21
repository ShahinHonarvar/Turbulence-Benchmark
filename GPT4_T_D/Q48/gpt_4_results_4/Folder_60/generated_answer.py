
def return_binary_or_hexa(numbers):
    a = numbers[38]
    b = numbers[52]
    sum_value = sum(set(range(a + 1, b)) - set(numbers[38:52]))
    if sum_value % 2 == 0:
        return hex(sum_value)[2:]
    else:
        return bin(sum_value)[2:]
