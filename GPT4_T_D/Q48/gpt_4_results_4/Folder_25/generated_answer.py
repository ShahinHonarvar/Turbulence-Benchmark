
def return_binary_or_hexa(numbers):
    a = numbers[37]
    b = numbers[43]
    missing_integers = set(range(a + 1, b)) - set(numbers[37:44])
    summation = sum(missing_integers)
    if summation % 2 != 0:
        return bin(summation)[2:]
    else:
        return hex(summation)[2:]
