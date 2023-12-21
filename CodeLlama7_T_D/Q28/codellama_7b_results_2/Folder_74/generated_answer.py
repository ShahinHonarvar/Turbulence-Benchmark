
def return_nth_smallest_ascii(s):
    # Create a dictionary to store the ASCII values of each character in the string
    ascii_values = {}

    # Iterate over each character in the string and add its ASCII value to the dictionary
    for char in s:
        ascii_values[char] = ord(char)

    # Sort the dictionary by value in ascending order
    sorted_values = sorted(ascii_values.items(), key=lambda x: x[1])

    # Return the character with the 6th smallest ASCII value
    return sorted_values[5][0]
