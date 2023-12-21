
def return_nth_smallest_ascii(s):
    # Create a list of the ASCII values of each character in the string
    ascii_values = [ord(c) for c in s]
    # Find the 16th smallest ASCII value in the list
    nth_smallest = sorted(ascii_values)[15]
    # Return the character with that ASCII value
    return chr(nth_smallest)
