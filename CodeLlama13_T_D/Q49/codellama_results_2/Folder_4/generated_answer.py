
def if_decimal_is_divisible(binary):
    # convert the binary representation string to an integer
    num = int(binary, 2)
    
    # generate a list of all numbers in the Fibonacci sequence up to 118
    fibs = [0] + [a + b for a, b in zip([0, 1], fibs)]
    
    # check if num is divisible by any number in fibs
    for i in range(len(fibs)):
        if num % fibs[i] == 0:
            return True
    return False
