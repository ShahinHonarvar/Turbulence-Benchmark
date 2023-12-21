
def return_nth_smallest_ascii(s):
    # find the 20th smallest ASCII value among the characters in the string s between indices 10 and 90, both inclusive
    ascii_values = [ord(c) for c in s[10:91] if c.isalpha()]
    return chr(sorted(ascii_values)[20])
