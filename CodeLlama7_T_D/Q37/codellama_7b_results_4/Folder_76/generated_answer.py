
def filter_chars(input_str):
    # Create an empty list to store the filtered characters
    filtered_chars = []
    # Iterate over each character in the input string
    for char in input_str:
        # Check if the current character is between indices 379 and 898, both inclusive
        if (input_str.index(char) >= 379) and (input_str.index(char) <= 898)):
            # Check if the current character is greater than or equal to character 'M' and smaller than or equal to character 'v'
            if (char >= 'M') and (char <= 'v'):
                # Remove all occurrences of the current character from the input string
                filtered_chars.append(input_str.replace(char, ''))
    return "".join(filtered_chars)
