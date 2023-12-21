
def return_nth_smallest_ascii(s):
    characters = list(set(s[47:71]))
    characters.sort(key=ord)
    return characters[13]
