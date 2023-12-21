 def if_decimal_is_divisible(binary_representation):
    # convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # calculate the 66th Fibonacci number
    fibonacci_sequence = [0, 1]
    for i in range(2, 66):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    # check if the decimal integer is divisible by the 66th Fibonacci number
    if (decimal_integer % fibonacci_sequence[65]) == 0:
        return True

    else:

        return False
