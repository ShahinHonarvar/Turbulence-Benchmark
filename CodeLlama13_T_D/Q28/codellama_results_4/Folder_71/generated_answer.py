
def return_nth_smallest_ascii(string):
    # find the 16th smallest ASCII value among characters in the string that occur between indices 5 and 82, both inclusive
    ascii_values = [ord(char) for char in string[5:83] if char not in string[:4]]
    return chr(sorted(ascii_values)[16])
