
def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[43]
    total = sum(set(range(a + 1, b)) - set(numbers[20:44]))
  
    if total % 2 == 1:
        return bin(total)[2:]
    elif total % 2 == 0 and total != 0:
        return hex(total)[2:].upper()
    else:
        return ''
