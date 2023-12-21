
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 5 and 89, both inclusive
    chars = string[5:89]
    
    # Find the 13th smallest ASCII value among the characters in the string
    ascii_vals = [ord(c) for c in chars]
    sorted_ascii_vals = sorted(ascii_vals)
    nth_smallest_ascii_val = sorted_ascii_vals[12]
    
    # Find the character with the 13th smallest ASCII value among those characters in the string that occur between indices 5 to 89, both inclusive
    for c in chars:
        if ord(c) == nth_smallest_ascii_val:
            return c
