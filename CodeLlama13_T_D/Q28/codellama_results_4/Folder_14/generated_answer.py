
def return_nth_smallest_ascii(string):
    # Find the 16th smallest ASCII value among characters in the string between indices 46 and 82, both inclusive
    ascii_values = [ord(c) for c in string[46:83] if c.isalpha()]
    return chr(sorted(ascii_values)[15])
