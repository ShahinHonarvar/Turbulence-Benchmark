
def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[7]
    integers = numbers[3:7]  # integers between indices 2 and 7
    
    sum_of_numbers = sum([i for i in range(a + 1, b) if i not in integers])
    
    if sum_of_numbers % 2 == 0:
        return hex(sum_of_numbers)[2:]
    else:
        return bin(sum_of_numbers)[2:]
