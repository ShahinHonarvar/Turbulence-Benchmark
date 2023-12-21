
def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    missing_nums = [num for num in range(a + 1, b) if num not in numbers[57:86]]
    sum_missing_nums = sum(missing_nums)
    
    if sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:].upper()
    else:
        return bin(sum_missing_nums)[2:]
