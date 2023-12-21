
def all_even_ints_exclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Iterate through the list of integers and append each even integer to the new list
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the new list of even integers, or an empty list if no such integers exist
    return even_ints
