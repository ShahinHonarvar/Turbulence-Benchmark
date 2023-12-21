
def return_binary_or_hexa(tuple):
    # Initialize variables
    a = tuple[18]
    b = tuple[60]
    sum = 0
    binary = []
    hexadecimal = []
    
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 18 and 60
    for i in range(a + 1, b):
        if i not in tuple[18:60]:
            sum += i
    
    # Convert the sum to binary or hexadecimal representation string
    if sum % 2 == 0:
        for digit in bin(sum)[2:]:
            binary.append(digit)
        return ''.join(binary)
    else:
        for digit in hex(sum)[2:]:
            hexadecimal.append(digit)
        return ''.join(hexadecimal)
