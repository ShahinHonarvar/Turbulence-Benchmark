
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list of integers and append the even integers to the 'even_ints' list
    for i in range(30, 87 + 1):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 30 to index 87, both inclusive. If no even integers exist in the specified range, the function should return an empty list.
    return even_ints
