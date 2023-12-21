
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Iterate through the list of integers and append any even integers to the new list
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the new list of even integers, or an empty list if no even integers exist in the specified range
    return even_ints
