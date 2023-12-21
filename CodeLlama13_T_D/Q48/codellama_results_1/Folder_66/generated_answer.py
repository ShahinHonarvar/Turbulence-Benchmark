
def return_binary_or_hexa(numbers):
    a = numbers[11] + 1
    b = numbers[76] - 1
    total = sum(i for i in range(a, b+1) if i not in set(numbers))
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
