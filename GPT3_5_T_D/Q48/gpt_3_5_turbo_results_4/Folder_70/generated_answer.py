
def return_binary_or_hexa(numbers):
    a = numbers[43]
    b = numbers[70]
    if b - a <= 1:
        return ""

    total_sum = sum(numbers[a+1:b])
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
