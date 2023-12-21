
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Loop through the list and check if each element is even

    for i in range(37, 52):

        if my_list[i] % 2 == 0:

            even_ints.append(my_list[i])

    return even_ints
