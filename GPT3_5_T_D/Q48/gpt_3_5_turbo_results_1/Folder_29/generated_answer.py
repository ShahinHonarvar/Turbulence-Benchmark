
def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[98]
    missing_numbers = [x for x in range(a+1, b) if x not in numbers[71:98]]
    sum_of_missing_numbers = sum(missing_numbers)
    
    if sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:]
    else:
        return bin(sum_of_missing_numbers)[2:]
