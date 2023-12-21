
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Find the first occurrence of the 115th Fibonacci number in the sequence
    fib_num = 0
    for i in range(len(str(decimal_int))):
        if str(decimal_int)[i] == '1' and str(decimal_int)[i+1] == '1':
            fib_num += 1
            if fib_num == 115:
                return True

    # If the number is not divisible by any Fibonacci number, return False

    return False
