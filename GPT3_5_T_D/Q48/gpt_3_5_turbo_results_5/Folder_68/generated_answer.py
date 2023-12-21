
def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[9]
    total_sum = sum(range(a+1, b))
    missing_sum = sum(numbers[1:9])
    if missing_sum == total_sum:
        return ""
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]
