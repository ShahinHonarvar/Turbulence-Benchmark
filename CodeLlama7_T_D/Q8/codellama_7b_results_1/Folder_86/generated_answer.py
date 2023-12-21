
def all_even_ints_exclusive(my_list):
    # Create a slice of the list starting at index 18 and ending before index 60
    even_ints = my_list[18:60]
    # Initialize an empty list to store the even integers
    result = []
    # Loop through the slice and append any even integers to the result list
    for i in even_ints:
        if i % 2 == 0:
            result.append(i)
    # Return the result list
    return result
