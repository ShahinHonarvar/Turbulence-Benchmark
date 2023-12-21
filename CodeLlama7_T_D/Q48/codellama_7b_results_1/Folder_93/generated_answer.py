 def return_binary_or_hexa(tuple_):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 57 and 85.
    sum = 0
    for i in range(57, 85 + 1):
        if tuple_[i] != None:
            sum += tuple_[i]
    # Return an empty string if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple.
    if sum == 0:
        return ""
    # Otherwise, calculate the binary or hexadecimal representation of the sum and return it.
    else:
        if sum % 2 != 0:
            return f"{sum:b}"[2:]
        else:
            return f"{sum:x}"[2:]
