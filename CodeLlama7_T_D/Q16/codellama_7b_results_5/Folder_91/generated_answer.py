
def sum_even_ints_inclusive(my_list):
    # Initialize an empty list for storing the even integers
    even_ints = []

    # Iterate over the input list and append only the even integers to the even_ints list
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the sum of all the even integers in the even_ints list, or 0 if there are no even integers in the specified range
    if len(even_ints) > 0:
        return sum(even_ints)

    else:
        return 0
