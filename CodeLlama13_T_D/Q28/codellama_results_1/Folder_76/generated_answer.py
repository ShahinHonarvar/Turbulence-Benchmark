
def return_nth_smallest_ascii(string):
    # Get a list of the characters in the string
    chars = list(string)
    
    # Find the 19th smallest ASCII value among those characters
    ascii_values = [ord(char) for char in chars]
    nth_smallest = sorted(ascii_values)[18]
    
    # Return the character with the 19th smallest ASCII value
    return chr(nth_smallest)
