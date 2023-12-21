
def return_binary_or_hexa(tuple_of_distinct_nonnegative_integers):
    # Get the indices of the first and last elements of the tuple
    first_index = 10
    last_index = 97
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 10 and 97
    sum_of_integers = 0
    for i in range(first_index + 1, last_index):
        if i not in tuple_of_distinct_nonnegative_integers:
            sum_of_integers += i
    # Return the binary or hexadecimal representation string of the sum, depending on whether it is an odd number or not
    if sum_of_integers % 2 == 0:
        return "{:x}".format(sum_of_integers)
    else:
        return "{:b}".format(sum_of_integers)
