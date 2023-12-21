
def return_nth_smallest_ascii(string):
    # Get the 11th smallest ASCII value among characters in string[25:46]
    ascii_values = [ord(char) for char in string[25:46]]
    nth_smallest = sorted(ascii_values)[10]
    
    # Return the character with that ASCII value
    return chr(nth_smallest)
