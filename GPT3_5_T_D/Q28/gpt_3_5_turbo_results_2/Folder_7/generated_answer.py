
def return_nth_smallest_ascii(s):
    substring = s[12:56]
    characters = sorted(set(substring))
    return characters[16]
