
def return_nth_smallest_ascii(string):
    substring = string[28:55]
    characters = sorted(set(substring))
    return characters[13]
