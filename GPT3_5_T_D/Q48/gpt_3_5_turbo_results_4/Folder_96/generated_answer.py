
def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[200]
    target_sum = 0

    for i in range(a + 1, b):
        if i not in numbers[51:200]:
            target_sum += i

    if target_sum == 0:
        return ""

    if target_sum % 2 == 1:
        return bin(target_sum)[2:]
    else:
        return hex(target_sum)[2:].upper()
