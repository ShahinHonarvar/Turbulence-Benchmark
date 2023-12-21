
def return_nth_smallest_ascii(s):
    characters = list(s[25:89])
    characters.sort(key=lambda x: ord(x))
    return characters[10]
