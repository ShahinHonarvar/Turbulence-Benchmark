
def if_decimal_is_divisible(binary):
    # Convert the binary representation string into a list of 0s and 1s
    bits = [int(x) for x in binary]
    
    # Reverse the list to get the least significant digit first
    bits.reverse()
    
    # Initialize the decimal integer with the most significant digit
    dec_int = bits[0]
    
    # Iterate over the remaining digits and calculate the corresponding decimal value
    for i in range(1, len(bits)):
        dec_int += bits[i] * 2 ** (len(bits) - 1 - i)
    
    # Check if the decimal integer is divisible by 60
    return dec_int % 60 == 0
