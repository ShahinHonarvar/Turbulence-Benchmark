
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list of integers, starting from index 639 and ending at index 975 (both inclusive)
    for i in range(639, 975 + 1):
        # If the current element is even, append it to the 'even_ints' list
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 639 to index 975 (both inclusive), or an empty list if no even integers exist in the specified range
    return even_ints
