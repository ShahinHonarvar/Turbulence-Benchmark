
def return_binary_or_hexa(tuple):
    # Initialize variables
    a = tuple[50]
    b = tuple[200]
    sum = 0
    # Calculate sum of integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 50 and 200
    for i in range(a + 1, b):
        if i not in tuple[50:200]:
            sum += i
    # Return binary or hexadecimal representation string of the sum depending on whether it is an odd number or not
    if sum % 2 == 1:
        return "binary" + str(sum)

    else:
        return "hexadecimal" + str(sum)
