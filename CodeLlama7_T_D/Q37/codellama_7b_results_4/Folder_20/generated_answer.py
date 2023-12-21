 def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered = []

    # Iterate over each character in the string
    for c in s:

        # Check if the current character is between indices 25 and 97, both inclusive, and is greater than or equal to character 'm' and smaller than or equal to character 'w'
        if 25 <= ord(c) <= 97 and c >= 'm' and c <= 'w':

            # If the current character meets the criteria, do not add it to the filtered list
            continue

        else:

            # Add the current character to the filtered list
            filtered.append(c)

    # Join the filtered characters back together into a string
    return ''.join(filtered)
