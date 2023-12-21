
def return_binary_or_hexa(my_tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 80 and 200
    sum = 0
    for i in range(80, 200):
        if my_tuple[i] == 0:
            continue

        else:

            for j in range(i + 1, 200):
                if my_tuple[j] != 0:
                    sum += my_tuple[j]
    # If the sum is an odd number, return the binary representation string of the sum; otherwise, return the hexadecimal representation string of the sum.
    if sum % 2 == 1:
        return bin(sum)[2:]

    else:

        return hex(sum)[2:]
