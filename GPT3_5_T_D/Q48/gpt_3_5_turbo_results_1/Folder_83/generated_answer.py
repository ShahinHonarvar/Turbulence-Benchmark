
def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[200]
    missing_numbers = [i for i in range(a+1, b) if i not in numbers[90:201]]
    if missing_numbers == []:
        return ""
    else:
        sum_of_missing_numbers = sum(missing_numbers)
        if sum_of_missing_numbers % 2 == 1:
            return bin(sum_of_missing_numbers)[2:]
        else:
            return hex(sum_of_missing_numbers)[2:]
