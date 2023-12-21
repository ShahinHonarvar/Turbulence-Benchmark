
def return_binary_or_hexa(numbers):
    a = numbers[3]
    b = numbers[8]
    absent_values = [x for x in range(a + 1, b) if x not in numbers[3:9]]
    if absent_values:
        total = sum(absent_values)
        if total % 2 == 0:
            return hex(total)[2:].upper()
        else:
            return bin(total)[2:]
    else:
        return ""
