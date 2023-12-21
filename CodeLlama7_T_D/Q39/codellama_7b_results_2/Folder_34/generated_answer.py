
def return_n_greatest_chars(input_string):
    # Initialize an empty list to store the sorted characters
    sorted_list = []

    # Iterate over each character in the input string
    for char in input_string:

        # If the character is already in the sorted list,
        # do nothing

        if char in sorted_list:
            continue


        # Otherwise, add the character to the sorted list and sort it in descending order

        sorted_list.append(char)
    sorted_list.sort(reverse=True)

    # Return the first 9 characters of the sorted list

    return sorted_list[:9]
