
def return_binary_or_hexa(my_tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 35 and 64.
    sum = 0
    for i in range(35, 64):
        if my_tuple[i] == 0:
            continue

        else:

            sum += my_tuple[i] - 1

    # Check if the sum is an odd number. If it is, return the binary representation string of the sum; otherwise, it should return the hexadecimal representation string of the sum.
    if sum % 2 == 0:
        return f'0x{sum:X}'

    else:

        return f'0b{sum:b}'
