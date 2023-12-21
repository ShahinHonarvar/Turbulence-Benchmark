
def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[52]
    num_set = set(numbers[37:52])
    total = sum(i for i in range(a+1, b) if i not in num_set)
    
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
