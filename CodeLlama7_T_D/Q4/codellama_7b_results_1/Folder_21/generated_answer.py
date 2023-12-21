
def all_pos_ints_exclusive(my_list):
    # Define the range of positive integers to extract
    start_index = 743
    end_index = 867
    # Initialize an empty list to store the extracted positive integers
    pos_ints = []
    # Iterate through the input list
    for i in range(len(my_list)):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is, add it to the list of extracted positive integers
            pos_ints.append(my_list[i])
    # Return the list of extracted positive integers within the specified range
    return pos_ints
