
def return_nth_smallest_ascii(string):
    substring = string[:46]
    characters = list(substring)
    characters.sort()
    return characters[9]
