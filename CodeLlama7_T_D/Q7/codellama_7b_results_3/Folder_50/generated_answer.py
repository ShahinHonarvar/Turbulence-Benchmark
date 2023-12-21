 def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list of integers from index 70 to index 84, both inclusive
    for i in range(70, 85):
        # Check if the current element is even and add it to the list of even integers if it is

        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 70 to index 84, both inclusive
    return even_ints
