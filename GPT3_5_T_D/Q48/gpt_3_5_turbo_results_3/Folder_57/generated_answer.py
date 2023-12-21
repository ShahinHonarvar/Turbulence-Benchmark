
def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    
    nums_in_range = set(numbers[26:80])
    
    total_sum = sum(i for i in range(a+1, b) if i not in nums_in_range)
    
    if total_sum % 2 == 1:
        binary = bin(total_sum)[2:]
        return binary
    else:
        hexa = hex(total_sum)[2:]
        return hexa.upper()
