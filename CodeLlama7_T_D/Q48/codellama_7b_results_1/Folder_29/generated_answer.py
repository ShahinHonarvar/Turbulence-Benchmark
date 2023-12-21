
def return_binary_or_hexa(tuple):
    # Check if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple
    if all(i in tuple for i in range(tuple[70], tuple[98] + 1)):
        return ""

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 70 and 98
    else:
        sum = 0

        for i in range(tuple[70] + 1, tuple[98]):
            if i not in tuple:
                sum += i

        # If the sum is an odd number, return the binary representation string of the sum; otherwise, return the hexadecimal representation string of the sum

        if sum % 2 == 1:
            return f"{sum:b}"[2:]

        else:
            return f"{sum:x}"[2:]
