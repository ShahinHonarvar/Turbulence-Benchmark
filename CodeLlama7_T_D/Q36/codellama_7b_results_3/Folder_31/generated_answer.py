 def filter_chars(my_string):
    # Create a new string that will hold the filtered characters
    filtered_string = ""
    # Loop through each character in the input string
    for char in my_string:
        # Check if the current character is between the indices 14 and 75 (both exclusive)
        if 14 < ord(char) < 75:
            # If it is, check if it is greater than '9' and smaller than 'K'
            if char > '9' and char < 'K':
                # If it is, remove all occurrences of that character within the string while keeping the order of all characters in the string intact
                filtered_string += char.replace(char, "")
            else:
                # If it is not greater than '9' and smaller than 'K', add the current character to the filtered string
                filtered_string += char
        else:
            # If the current character is not between the indices 14 and 75 (both exclusive), add the current character to the filtered string
            filtered_string += char
    return filtered_string
