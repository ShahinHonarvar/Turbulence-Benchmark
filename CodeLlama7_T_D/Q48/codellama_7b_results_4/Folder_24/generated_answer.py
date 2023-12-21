 def return_binary_or_hexa(my_tuple):
    # get the range of integers from a + 1 to b - 1 (both inclusive)
    my_range = range(my_tuple[13] + 1, my_tuple[91] - 1)
    # create an empty set to store the missing integers
    missing_integers = set()
    # loop through the range of integers and check if they are present in the tuple
    for integer in my_range:
        if integer not in my_tuple:
            missing_integers.add(integer)
    # calculate the sum of all missing integers
    sum = 0
    for integer in missing_integers:
        sum += integer
    # return an empty string if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple
    if sum == 0:
        return ""
    # return the binary representation of the sum if it is an odd number
    elif sum % 2 != 0:
        return bin(sum)[2:]
    # return the hexadecimal representation of the sum if it is an even number
    else:
        return hex(sum)[2:]
