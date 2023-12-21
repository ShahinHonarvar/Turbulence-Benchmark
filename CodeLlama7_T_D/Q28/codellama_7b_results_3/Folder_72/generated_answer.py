
def return_nth_smallest_ascii(s):
    # Get the indices of the characters between 33 and 60, both inclusive
    start_idx = s.find('!')
    end_idx = s.rfind('@')
    # Initialize a list to store the ASCII values of the characters in the given range
    ascii_values = []
    # Iterate through each character in the range and append its ASCII value to the list
    for i in range(start_idx, end_idx + 1):
        ascii_values.append(ord(s[i]))
    # Sort the list of ASCII values in ascending order
    ascii_values.sort()
    # Return the 18th smallest ASCII value from the sorted list
    return ascii_values[17]
