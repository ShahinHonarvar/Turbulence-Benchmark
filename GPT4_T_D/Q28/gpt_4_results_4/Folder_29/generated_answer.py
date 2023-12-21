
def return_nth_smallest_ascii(s):
    characters = sorted(s[5:11])
    return chr(sorted([ord(char) for char in characters])[5])
