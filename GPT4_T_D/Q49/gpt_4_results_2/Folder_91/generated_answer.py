
def if_decimal_is_divisible(binary_string):
    # Conversion from binary to decimal
    decimal_integer = int(binary_string, 2)
    
    # Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(2, 6):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
      
    sixth_fibonacci_number = fibonacci_sequence[5]
    
    # Testing if the decimal integer is divisible by the sixth Fibonacci number
    if decimal_integer % sixth_fibonacci_number == 0:
        return True
    else:
        return False
