
def return_nth_smallest_ascii(s):
    s = s[60:89]  # Extract characters between indices 60 and 88 (both inclusive)
    s = sorted(s)  # Sort the characters in ascending ASCII order
    return s[6]  # Return the character with the 7th smallest ASCII value
