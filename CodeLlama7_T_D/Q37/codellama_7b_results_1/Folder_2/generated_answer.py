
def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the string
    for char in s:

        # Check if the current character is between indices 477 and 984, both inclusive
        if 477 <= s.index(char) <= 984:

            # Check if the current character is greater than or equal to ',' and smaller than or equal to 'V'
            if char >= ',' and char <= 'V':

                # Do not add the current character to the filtered characters list
                continue


        # Add the current character to the filtered characters list
        filtered_chars.append(char)

    # Join the filtered characters list into a single string
    return ''.join(filtered_chars)
