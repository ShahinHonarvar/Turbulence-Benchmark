
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[70]
    range_numbers = set(numbers[14:70])
    total_sum = sum(i for i in range(a+1, b) if i not in range_numbers)

    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
