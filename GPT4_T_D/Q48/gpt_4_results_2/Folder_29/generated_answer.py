
def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[98]
    missing_nums_sum = sum(set(range(a + 1, b)) - set(numbers[70:98]))
    if missing_nums_sum % 2 == 0: # sum is even
        return hex(missing_nums_sum)[2:]
    else: # sum is odd
        return bin(missing_nums_sum)[2:]
