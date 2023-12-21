
def return_nth_smallest_ascii(string):
    substring = string[51:90]
    unique_characters = set(substring)
    sorted_characters = sorted(unique_characters)
    return sorted_characters[13]
