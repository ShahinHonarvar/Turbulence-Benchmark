
def return_nth_smallest_ascii(string):
    subset = string[1:37]
    characters = sorted(set(subset))
    return characters[14]
