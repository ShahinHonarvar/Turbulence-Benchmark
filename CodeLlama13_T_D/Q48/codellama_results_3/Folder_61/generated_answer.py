
def return_binary_or_hexa(numbers):
    sum = 0
    for i in range(a + 1, b - 1):
        if i not in numbers:
            sum += i
    if sum % 2 == 0:
        return f"{sum:X}"
    else:
        return bin(sum)[2:]
