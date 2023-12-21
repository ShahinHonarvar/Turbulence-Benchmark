
def return_binary_or_hexa(my_tuple):
    # check if all integers from a + 1 to b - 1 are present in the specified range in the tuple
    all_ints = set(range(my_tuple[20], my_tuple[43] + 1)))
    if all_ints == set(my_tuple):
        return ""

    # calculate sum of integers not present in the tuple between indices 20 and 43
    sum = 0
    for i in range(my_tuple[20] + 1, my_tuple[43]):
        if i not in my_tuple:
            sum += i

    # return binary or hexadecimal representation string of the sum
    if sum % 2 == 1:
        return bin(sum)[2:]

    else:

        return hex(sum)[2:].upper()
