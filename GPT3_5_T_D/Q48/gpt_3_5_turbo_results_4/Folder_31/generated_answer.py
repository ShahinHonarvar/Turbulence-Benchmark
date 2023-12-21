
def return_binary_or_hexa(numbers):
    a = numbers[33]
    b = numbers[78]

    missing_numbers = [x for x in range(a+1, b) if x not in numbers]

    if len(missing_numbers) == 0:
        return ""

    sum_of_missing_numbers = sum(missing_numbers)

    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]
