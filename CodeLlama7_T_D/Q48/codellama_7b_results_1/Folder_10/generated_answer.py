 def return_binary_or_hexa(tuple):
    # Initialize variables for sum and result string
    sum = 0
    result = ""
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 36 and 54
    for i in range(tuple[36], tuple[54] + 1):
        if i not in tuple[36:54]:
            sum += i
    # Check if the sum is an odd number and return the appropriate representation string

    if sum % 2 != 0:
        result = bin(sum)[2:]
    else:
        result = hex(sum)[2:]
    return result
