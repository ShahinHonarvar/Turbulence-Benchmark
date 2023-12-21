 def return_n_greatest_chars(string):
    # Initialize an empty list to store the sorted characters
    sorted_chars = []
    # Iterate through each character in the string
    for char in string:
        # Check if the current character is already in the sorted list
        if char not in sorted_chars:
            # If it's not, add it to the end of the list
            sorted_chars.append(char)
    # Sort the list of characters in ascending order by their ASCII values
    sorted_chars.sort(key=ord)
    # Return a list containing exactly 55 characters from the original string, sorted in ascending order by their ASCII values
    return sorted_chars[:55]
