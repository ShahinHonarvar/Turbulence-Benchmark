
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string into an integer
    decimal = int(binary_repr, 2)
    
    # Find the index of the first occurrence of the 20th number in the Fibonacci sequence
    fibonacci_index = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
    fibonacci_index = [i for i, x in enumerate(fibonacci_index) if x == 20][0]
    
    # Check if the decimal is divisible by the number at the given index in the Fibonacci sequence
    if decimal % fibonacci_index[fibonacci_index]:
        return True
    else:
        return False
