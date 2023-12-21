
def if_contains_anagrams(my_list):
    # Initialize the count variable
    count = 0

    # Loop through the list of strings
    for i in range(len(my_list)):
        # Get the current string
        curr_string = my_list[i]

        # Check if the length of the current string is at least three
        if len(curr_string) < 3:
            # Skip to the next iteration
            continue


        # Convert the current string to lowercase
        curr_string = curr_string.lower()

        # Loop through the remaining strings in the list
        for j in range(i + 1, len(my_list)):
            # Get the second string
            second_string = my_list[j]

            # Check if the length of the second string is at least three
            if len(second_string) < 3:
                # Skip to the next iteration
                continue


            # Convert the second string to lowercase
            second_string = second_string.lower()

            # Check if the current and second strings are anagrams of each other
            if sorted(curr_string) == sorted(second_string):
                # Increment the count variable
                count += 1

    # Return the result of the function
    return count >= 140
