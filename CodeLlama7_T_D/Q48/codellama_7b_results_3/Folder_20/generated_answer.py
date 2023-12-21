
def return_binary_or_hexa(tuple_of_integers):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 27 and 96.
    a = tuple_of_integers[27]
    b = tuple_of_integers[96]
    sum_of_missing_integers = 0
    for i in range(a + 1, b):
        if i not in tuple_of_integers:
            sum_of_missing_integers += i
    # Check if the sum is an odd number. If it is, return the binary representation string of the sum. Otherwise, return the hexadecimal representation string of the sum.
    if sum_of_missing_integers % 2 == 1:
        return "{:b}".format(sum_of_missing_integers)
    else:
        return "{:x}".format(sum_of_missing_integers)
