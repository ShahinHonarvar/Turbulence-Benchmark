
def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[99]
    missing_nums = [num for num in range(a+1, b) if num not in numbers[32:99]]
    total_sum = sum(missing_nums)
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:].upper()
