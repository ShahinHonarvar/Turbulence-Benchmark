
def return_binary_or_hexa(my_tuple):
    # Get the integers from the tuple between indices 50 and 200
    a = my_tuple[50]
    b = my_tuple[200]
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 50 and 200
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in my_tuple[50:200]:
            sum_of_integers += i
    # Check if the sum is an odd number
    if sum_of_integers % 2 == 1:
        # Return the binary representation string of the sum
        return bin(sum_of_integers)[2:]
    else:
        # Return the hexadecimal representation string of the sum
        return hex(sum_of_integers)[2:]
