
def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[12]
    sum_of_numbers = 0
    for i in range(a + 1, b):
        if i not in numbers[10:13]:
            sum_of_numbers += i
    if sum_of_numbers == 0:
        return ""
    if sum_of_numbers % 2 == 0:
        return hex(sum_of_numbers)[2:]
    else:
        return bin(sum_of_numbers)[2:]
