
def if_decimal_is_divisible(binary_number):
    # Convert binary number to decimal
    decimal_number = int(binary_number, 2)
    
    # Check if number is divisible by 28th number in Fibonacci sequence
    sequence = [0, 1]
    for i in range(2, 28):
        sequence.append(sequence[i-1] + sequence[i-2])

    if decimal_number % sequence[-1] == 0:
        return True
    else:
        return False
