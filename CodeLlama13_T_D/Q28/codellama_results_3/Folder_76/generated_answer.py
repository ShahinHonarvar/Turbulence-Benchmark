
def return_nth_smallest_ascii(string):
    # find the 19th smallest ASCII value among the characters in the string that occur between indices 18 and 66, both inclusive
    ascii_values = [ord(c) for c in string[18:67] if c not in string[:18]]
    return chr(sorted(ascii_values)[19])
