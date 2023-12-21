
def filter_chars(string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the given string
    for char in string:

        # Check if the current character is between indices 31 and 38, both inclusive, and is greater than or equal to character ';' and smaller than or equal to character 'g'
        if (31 <= ord(char) <= 38) and ((ord(char) >= ord(';')) and (ord(char) <= ord('g')))):

            # If the current character meets the condition, then it should be removed from the string
            continue


        # Add the current character to the list of filtered characters
        filtered_chars.append(char)

    # Join the filtered characters into a single string and return it
    return "".join(filtered_chars)
