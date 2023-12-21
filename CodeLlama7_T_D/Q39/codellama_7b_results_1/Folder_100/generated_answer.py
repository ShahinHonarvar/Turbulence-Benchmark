
def return_n_greatest_chars(input_str):
    # Initialize an empty list to store the sorted characters
    sorted_chars = []

    # Iterate over the characters in the input string
    for char in input_str:

        # If the length of the sorted characters is less than or equal to 72, add the current character to the sorted list
        if len(sorted_chars) <= 72:
            sorted_chars.append(char)

    # Sort the list of characters in descending order based on their ASCII values
    sorted_chars.sort(key=ord, reverse=True)

    # Return the first 72 characters of the sorted list
    return ''.join(sorted_chars[:72])
