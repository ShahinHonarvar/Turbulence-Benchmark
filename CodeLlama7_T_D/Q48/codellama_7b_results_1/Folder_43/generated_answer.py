
def return_binary_or_hexa(tuple):
    # Get the indices of the first and last integers in the tuple
    start_index = tuple.index(a) + 1
    end_index = tuple.index(b) - 1
    # Calculate the sum of all integers between a + 1 and b - 1 that are not present in the tuple
    sum = 0
    for i in range(start_index, end_index + 1):
        if tuple[i] not in range(a + 1, b):
            sum += tuple[i]
    # Check if the sum is an odd number and return the appropriate representation string

    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
