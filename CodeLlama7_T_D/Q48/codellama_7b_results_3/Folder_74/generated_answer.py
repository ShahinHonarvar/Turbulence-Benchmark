
def return_binary_or_hexadecimal(my_tuple):
    # Extract the integers from the tuple between indices 69 and 97
    a = my_tuple[69]
    b = my_tuple[97]

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 69 and 97.
    sum = 0
    for i in range(a + 1, b):
        if i not in my_tuple[69:97]:
            sum += i

    # If the sum is an odd number, return the binary representation string of the sum; otherwise, return the hexadecimal representation string of the sum.
    if sum % 2 == 1:
        return f"{sum:b}"

    else:

        return f"{sum:x}"
