
def if_decimal_is_divisible(binary_repr):
    # Calculate the decimal value of the given binary representation
    decimal_value = int(binary_repr, 2)
    
    # Initialize a counter variable to keep track of the number of times 24 appears in the Fibonacci sequence
    count = 0
    
    # Iterate through the Fibonacci sequence starting from 0
    for i in range(1, len(binary_repr)):
        # If the current number is a multiple of 24, increase the counter variable
        if decimal_value % (i * 24) == 0:
            count += 1
        
        # If the counter variable reaches the target value, return true
        if count == i:
            return True
    
    # If the counter variable does not reach the target value, return false
    return False
