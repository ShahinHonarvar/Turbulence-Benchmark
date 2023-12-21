
def return_binary_or_hexa(tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 73 and 84.
    sum = 0
    for i in range(73, 85):
        if tuple[i] == 0:
            continue

        else:

            for j in range(73 + 1, 84 - 1 + 1):
                if tuple[j] == 0:
                    sum += 1

    # If the sum is an odd number, return the binary representation string of the sum; otherwise, return the hexadecimal representation string of the sum.
    if sum % 2 != 0:
        return bin(sum)[2:]

    else:

        return hex(sum)[2:].upper()
