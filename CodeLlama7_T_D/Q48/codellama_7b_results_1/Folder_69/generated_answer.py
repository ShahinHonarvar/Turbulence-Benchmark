
def return_binary_or_hexa(my_tuple):
    # Get the indices of the first and last elements in the tuple
    first_index = my_tuple.index(my_tuple[0])
    last_index = my_tuple.index(my_tuple[-1])
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 39 and 43
    sum = 0
    for i in range(first_index + 1, last_index):
        if my_tuple[i] not in my_tuple[first_index:last_index]:
            sum += my_tuple[i]
    # Check if the sum is an odd number
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
