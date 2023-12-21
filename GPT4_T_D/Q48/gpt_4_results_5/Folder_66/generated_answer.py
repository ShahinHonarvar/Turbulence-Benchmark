
def return_binary_or_hexa(numbers):
    a = numbers[11]
    b = numbers[76]
    total = sum(set(range(a + 1, b)) - set(numbers[11:76]))
    return bin(total)[2:] if total % 2 else hex(total)[2:]
