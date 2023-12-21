
def return_binary_or_hexa(tuple):
    # Initialize variables
    sum = 0
    binary = ''
    hexa = ''
    
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 20 and 51
    for i in range(tuple[20] + 1, tuple[51] - 1):
        if i not in tuple[20:51]:
            sum += i
    
    # Determine whether the sum is an odd number
    if sum % 2 == 1:
        
        # Convert the sum to a binary representation string
        for digit in bin(sum)[2:]:
            
            # Append each digit to the binary representation string
            binary += digit
            
        # Return the binary representation string
        return binary
            
    else:
            
        # Convert the sum to a hexadecimal representation string
        for digit in hex(sum)[2:]:
            
            # Append each digit to the hexadecimal representation string
            hexa += digit
            
        # Return the hexadecimal representation string
        return hexa
