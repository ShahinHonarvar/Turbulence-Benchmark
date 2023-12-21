
def return_nth_smallest_ascii(s):
    substring = s[60:89] # get the substring between indices 60 to 88
    substring = sorted(substring) # sort the substring in ascending order
    return substring[6] # return the character at index 6 (7th smallest ASCII value)
