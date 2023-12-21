
def return_nth_smallest_ascii(string):
    substring = string[29:48]
    characters = list(set(substring))
    characters.sort(key=lambda x: ord(x))
    return characters[6]
