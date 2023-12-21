
def return_binary_or_hexa(my_tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 13 and 70.
    a = my_tuple[13]
    b = my_tuple[70]
    sum = 0
    for i in range(a + 1, b):
        if i not in my_tuple:
            sum += i
    # If the sum is an odd number, return the binary representation string of the sum. Otherwise, return the hexadecimal representation string of the sum.
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)
