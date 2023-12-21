
def return_binary_or_hexa(my_tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 0 and 9.
    sum = 0
    for i in range(len(my_tuple)):
        if my_tuple[i] == 0 or my_tuple[i] == len(my_tuple) - 1:
            continue

        else:

            sum += my_tuple[i + 1] - my_tuple[i - 1]
    # If the sum is an odd number, return its binary representation string; otherwise, return its hexadecimal representation string.
    if sum % 2 == 0:
        return f"{hex(sum)[2:]}"

    else:

        return f"{bin(sum)[3:]}"
