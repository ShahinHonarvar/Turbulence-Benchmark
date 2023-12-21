
def return_nth_smallest_ascii(s):
    # sort the string in ascending order
    s = sorted(s)
    # get the character with the 4th smallest ASCII value among those characters in the string that occur between indices 0 to 4, both inclusive.
    return s[3]
