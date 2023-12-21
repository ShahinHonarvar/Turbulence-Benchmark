
def return_nth_smallest_ascii(s):
    characters_substring = s[29:34]
    sorted_characters = sorted(characters_substring, key=ord)
    return sorted_characters[4]
