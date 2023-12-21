
def all_even_ints_exclusive(my_list):
    # Check if the list is empty or has less than 55 elements
    if len(my_list) < 55:
        return []

    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list and append the even integers to the list
    for i in range(55, len(my_list)):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    return even_ints
