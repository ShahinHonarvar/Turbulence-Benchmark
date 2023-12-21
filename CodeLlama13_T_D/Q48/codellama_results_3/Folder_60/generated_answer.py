
def return_binary_or_hexa(my_tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 38 and 52
    sum = my_tuple[38] - 1 + my_tuple[52] - my_tuple[38] - 1
    
    # Check if the sum is an odd number
    if sum % 2 == 0:
        # Return the hexadecimal representation string of the sum
        return hex(sum)[2:]
    else:
        # Return the binary representation string of the sum
        return bin(sum)[2:]
