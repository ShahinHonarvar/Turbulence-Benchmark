
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list of integers and check if each integer is even

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 0 to index 10, both exclusive

    return even_ints
