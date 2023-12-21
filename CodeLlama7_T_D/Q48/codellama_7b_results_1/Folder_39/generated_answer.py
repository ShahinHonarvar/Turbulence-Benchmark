
def return_binary_or_hexa(tuple):
    # Initialize variables
    sum = 0
    binary = ''
    hexa = ''
    
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 44 and 91.
    for i in range(tuple[44], tuple[91]):
        if i not in tuple:
            sum += i
    
    # Check if the sum is an odd number
    if sum % 2 == 1:
        
        # If it is, return the binary representation string of the sum.
        for digit in bin(sum)[2:]:
            binary += digit
            
        # Return the binary representation string with no prefix and start with the most significant digit.
        return binary
        
    else:
        
        # If it is not, return the hexadecimal representation string of the sum.
        for digit in hex(sum)[2:]:
            hexa += digit
            
        # Return the hexadecimal representation string with no prefix and start with the most significant digit.
        return hexa
