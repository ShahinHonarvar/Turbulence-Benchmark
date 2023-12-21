
def return_nth_smallest_ascii(s):
    substring = s[42:60]
    sorted_characters = sorted(substring, key=ord)
    return sorted_characters[16]
