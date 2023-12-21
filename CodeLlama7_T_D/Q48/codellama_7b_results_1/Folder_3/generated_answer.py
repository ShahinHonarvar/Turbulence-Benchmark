
def return_binary_or_hexa(my_tuple):
    # Get the starting and ending indices of the specified range
    start = my_tuple[56] + 1
    end = my_tuple[88] - 1
    # Calculate the sum of all integers in the specified range that are not present in the tuple between indices 56 and 88
    sum = 0
    for i in range(start, end + 1):
        if i not in my_tuple[56:88]:
            sum += i
    # Return the binary or hexadecimal representation of the sum, depending on whether it is an odd number
    if sum % 2 == 0:
        return f"{hex(sum)[2:]}"
    else:
        return f"{bin(sum)[3:]}"
