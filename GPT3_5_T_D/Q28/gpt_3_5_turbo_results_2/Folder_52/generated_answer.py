
def return_nth_smallest_ascii(s):
    substring = s[46:73]
    characters = list(substring)
    sorted_chars = sorted(characters, key=lambda c: ord(c))
    return sorted_chars[14]
