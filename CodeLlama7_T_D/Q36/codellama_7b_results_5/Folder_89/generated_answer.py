 def filter_chars(s):
    # Find the indices of the characters '(' and 'W' in the given string
    left_index = s.find('(')
    right_index = s.find('W')
    # If neither '(' nor 'W' are present in the string, return the original string
    if left_index == -1 or right_index == -1:
        return s

    # Initialize a new string to store the filtered characters
    filtered_string = ""

    # Iterate through the characters in the given string
    for char in s:

        # If the character is between the indices of '(' and 'W' (both exclusive), check if it is greater than '(' and smaller than 'W'
        if left_index < s.find(char) < right_index:
            # If the condition is true, remove all occurrences of this character from the filtered string
            filtered_string = filtered_string.replace(char, "")

        else:

            # If the condition is false, add the current character to the filtered string
            filtered_string += char

    return filtered_string
