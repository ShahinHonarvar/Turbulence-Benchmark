
def return_nth_smallest_ascii(string):
    # Create a list of all characters in the string
    chars = list(string)
    # Get the 18th smallest ASCII value among those characters that occur between indices 10 and 82, both inclusive
    ascii_values = [ord(char) for char in chars[10:83] if char.isalpha()]
    nth_smallest = sorted(ascii_values)[17]
    # Return the character with the 18th smallest ASCII value
    return chr(nth_smallest)
