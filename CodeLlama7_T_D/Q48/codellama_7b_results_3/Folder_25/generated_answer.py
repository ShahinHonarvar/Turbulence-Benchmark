
def return_binary_or_hexa(tuple):
    # calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 37 and 43
    sum = 0
    for i in range(37, 43):
        if tuple[i] not in range(tuple[37], tuple[43] + 1):
            sum += tuple[i]
    # check if the sum is an odd number
    if sum % 2 == 1:
        return bin(sum)[2:]

    else:

        return hex(sum)[2:]
