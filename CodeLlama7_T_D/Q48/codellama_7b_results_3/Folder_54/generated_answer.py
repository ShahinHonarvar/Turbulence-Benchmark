
def return_binary_or_hexa(my_tuple):
    # Check if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple
    if len(set(range(my_tuple[35] + 1, my_tuple[64] - 1))) == 0:
        return ""
    
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 35 and 64
    sum = 0
    for i in range(my_tuple[35] + 1, my_tuple[64] - 1):
        if i not in set(range(my_tuple[35], my_tuple[64]))):
            sum += i
    
    # Check if the sum is an odd number and return the binary or hexadecimal representation string accordingly

    if sum % 2 == 1:
        return "{:b}".format(sum)
    else:
        return "{:x}".format(sum)
