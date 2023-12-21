 def filter_chars(s):
    # Create a new list to store the filtered characters
    filtered_chars = []
    # Iterate over each character in the string
    for char in s:
        # Check if the current character is between the indices 49 and 56 (both exclusive)
        if 49 < ord(char) < 57:
            # If the character is between these indices, check if it is greater than 'I' and smaller than 'a'
            if char > 'I' and char < 'a':
                # If the condition is true, continue to the next iteration of the loop
                continue

        # If the current character does not meet the conditions, add it to the filtered_chars list
        filtered_chars.append(char)
    # Join the filtered characters into a string and return it
    return ''.join(filtered_chars)
