
def if_decimal_is_divisible(binary_representation):
    fibonacci = [0, 1]  # Fibonacci sequence starting from 0, 1
    n = 2
    while len(fibonacci) <= 177:  # Generate Fibonacci sequence up to the 177th number
        fibonacci.append(fibonacci[n-1] + fibonacci[n-2])
        n += 1
    
    decimal_integer = int(binary_representation, 2)  # Convert binary representation to decimal integer
    
    return decimal_integer % fibonacci[177] == 0
