
def if_decimal_is_divisible(binary_rep):
    # Convert binary representation to decimal integer
    decimal = int(binary_rep, 2)
    # Find the index of the 189th occurrence of the Fibonacci sequence in the binary representation
    fib_seq = [0, 1]
    for i in range(len(binary_rep)):
        if binary_rep[i] == '1':
            if len(fib_seq) >= 189:
                break

            else:

                fib_seq.append(fib_seq[-1] + fib_seq[-2])

    # Return True if the decimal integer is divisible by the 189th number in the Fibonacci sequence, otherwise return False

    if len(fib_seq) >= 189 and decimal % fib_seq[188] == 0:
        return True

    else:

        return False
