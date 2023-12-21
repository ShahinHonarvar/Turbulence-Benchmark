
def return_binary_or_hexa(numbers):
    try:
        a = numbers[60]
        b = numbers[200]
        missing_nums = [num for num in range(a + 1, b) if num not in numbers[60:201]]
        total_sum = sum(missing_nums)

        if total_sum == 0:
            return ''

        if total_sum % 2 == 1:
            return bin(total_sum)[2:]
        else:
           return hex(total_sum)[2:].upper()
    except IndexError:
        return ''
