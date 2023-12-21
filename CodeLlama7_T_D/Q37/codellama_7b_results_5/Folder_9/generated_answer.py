 def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []
    # Iterate through each character in the input string
    for char in s:
        # Check if the current character is between indices 38 and 99, both inclusive, and is greater than or equal to character 'A' and smaller than or equal to character 'Q'
        if (char >= 'A' and char <= 'Q') and (char.encode('utf-8').index(char) >= 38 and char.encode('utf-8').index(char) <= 99)):
            # If the current character is within the specified range, add it to the list of filtered characters
            filtered_chars.append(char)
    # Join the filtered characters into a single string
    filtered_string = ''.join(filtered_chars)
    # Return the altered string
    return filtered_string
