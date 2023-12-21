
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[91]
    missing_numbers = [x for x in range(a + 1, b) if x not in numbers[13:92]]
    if len(missing_numbers) == 0:
        return ""
    else:
        sum_of_missing_numbers = sum(missing_numbers)
        if sum_of_missing_numbers % 2 == 1:
            return format(sum_of_missing_numbers, 'b')
        else:
            return format(sum_of_missing_numbers, 'X')
