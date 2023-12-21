
def return_binary_or_hexa(tuple):
    # initialize variables for sum and oddness check
    sum = 0
    is_odd = False

    # calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 50 and 200
    for i in range(tuple[50] + 1, tuple[200] - 1):
        # check if integer is not present in the tuple between indices 50 and 200
        if i not in tuple[50:200]:
            # add integer to sum if it is not present in the tuple
            sum += i

    # check if sum is an odd number
    if sum % 2 == 1:
        # return binary representation of sum if it is an odd number
        return bin(sum)[2:]

    else:
        # return hexadecimal representation of sum if it is an even number
        return hex(sum)[2:]
