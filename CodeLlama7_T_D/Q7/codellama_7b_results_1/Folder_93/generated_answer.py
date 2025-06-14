
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list starting from index 75
    for i in range(75, len(my_list)):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # Add the current element to the list of even integers
            even_ints.append(my_list[i])
    return even_ints
