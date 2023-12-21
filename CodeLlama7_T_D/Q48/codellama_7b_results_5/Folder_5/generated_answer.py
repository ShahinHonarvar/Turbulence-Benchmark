
def return_binary_or_hexa(my_tuple):
    # Get the integers from the tuple
    a = my_tuple[2]
    b = my_tuple[8]
    # Calculate the sum of all integers from a + 1 to b - 1 that are not present in the tuple between indices 2 and 8
    sum = 0
    for i in range(a + 1, b):
        if i not in my_tuple:
            sum += i
    # Check if the sum is an odd number
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
