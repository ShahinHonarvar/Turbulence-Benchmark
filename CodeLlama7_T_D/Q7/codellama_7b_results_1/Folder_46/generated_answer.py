
def all_even_ints_inclusive(my_list):
    # Define the start and end indices for the range of even integers
    start = 30
    end = 87
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list from the start index to the end index
    for i in range(start, end+1):
        # If the current element is even, add it to the list of even integers
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 30 to index 87, both inclusive
    return even_ints
