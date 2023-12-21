
def return_binary_or_hexa(my_tuple):
    # Get the integers between indices 25 and 80
    a = my_tuple[25]
    b = my_tuple[80]
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 25 and 80
    sum = 0
    for i in range(a + 1, b):
        if i not in my_tuple[25:80]:
            sum += i
    # Return an empty string if all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple
    if sum == 0:
        return ""
    # Otherwise, return the binary or hexadecimal representation string of the sum
    elif sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
