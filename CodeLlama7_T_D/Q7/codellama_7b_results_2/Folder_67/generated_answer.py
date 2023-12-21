
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []
    # Iterate through the list of integers starting from index 22 and ending at index 50, both inclusive
    for i in range(22, 51):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 22 to index 50, both inclusive
    return even_ints
