
def return_binary_or_hexa(numbers):
    a = numbers[427]
    b = numbers[669]
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in numbers[428:669]:
            missing_numbers.append(i)
    if len(missing_numbers) == 0:
        return ""
    else:
        sum_missing = sum(missing_numbers)
        if sum_missing % 2 == 1:
            return bin(sum_missing)[2:]
        else:
            return hex(sum_missing)[2:]
