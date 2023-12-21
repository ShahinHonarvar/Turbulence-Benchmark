
def return_binary_or_hexa(tuple):
    # Initialize variables for sum and number of integers in range
    sum = 0
    num_ints = 0

    # Iterate through tuple and calculate sum of integers between indices 57 and 84
    for i in range(57, 85):
        if tuple[i] not in range(a + 1, b - 1):
            sum += tuple[i]
            num_ints += 1

    # Return empty string if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple
    if num_ints == 0:
        return ""

    # If sum is odd, return binary representation string of sum
    elif sum % 2 != 0:
        return "".join(str((sum + 1) >> i) for i in range(32)).rstrip('0'))

    # Otherwise, return hexadecimal representation string of sum
    else:
        return "0x" + "".join(hex(sum >> (i * 4))[2:]).rstrip('0'))
