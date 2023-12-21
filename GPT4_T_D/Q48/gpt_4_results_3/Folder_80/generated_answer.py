
def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[84]
    sum_of_integers = sum(set(range(a + 1, b)) - set(numbers[57:85]))
    
    if sum_of_integers != 0:
        if sum_of_integers % 2 == 1:
            return bin(sum_of_integers)[2:]
        else:
           return hex(sum_of_integers)[2:].upper()
    else:
        return ""
