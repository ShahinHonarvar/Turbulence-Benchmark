
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    chars = list(string)
    # Create a dictionary to store the ASCII values and their counts
    ascii_counts = {}
    for char in chars:
        ascii_value = ord(char)
        if ascii_value not in ascii_counts:
            ascii_counts[ascii_value] = 0
        ascii_counts[ascii_value] += 1
    # Get the ASCII values between indices 13 and 35, both inclusive
    filtered_ascii_values = [ascii_value for ascii_value in ascii_counts if 13 <= ascii_value <= 35]
    # Sort the list of ASCII values
    sorted_ascii_values = sorted(filtered_ascii_values)
    # Return the character with the 18th smallest ASCII value
    return chr(sorted_ascii_values[17])
