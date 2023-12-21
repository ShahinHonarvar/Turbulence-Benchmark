
def return_nth_smallest_ascii(string):
    # Calculate the 13th smallest ASCII value among those characters in the string that occur between indices 1 and 46, both inclusive
    nth_smallest = sorted([ord(char) for char in string[1:47]])[12]
    
    # Return the character with the calculated ASCII value
    return chr(nth_smallest)
