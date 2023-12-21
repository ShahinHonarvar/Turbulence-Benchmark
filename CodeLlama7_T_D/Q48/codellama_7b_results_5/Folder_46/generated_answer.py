
def return_binary_or_hexa(my_tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 10 and 79
    sum = 0
    for i in range(10, 79):
        if my_tuple[i] != 0:
            sum += i - 9
    # Check if the sum is an odd number
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
