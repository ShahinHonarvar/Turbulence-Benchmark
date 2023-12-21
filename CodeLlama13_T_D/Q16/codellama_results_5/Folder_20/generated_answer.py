
def sum_even_ints_inclusive(my_list):
    # initialize a variable to store the sum of even integers
    sum_of_evens = 0

    # iterate over the list from index 56 to index 66, both inclusive
    for i in range(56, 67):
        # check if the current element is even and add it to the sum
        if my_list[i] % 2 == 0:
            sum_of_evens += my_list[i]

    # return the sum of all even integers from index 56 to index 66, both inclusive
    return sum_of_evens
