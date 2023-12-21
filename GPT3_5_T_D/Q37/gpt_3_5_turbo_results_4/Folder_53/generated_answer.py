
def filter_chars(string):
    characters_to_remove = ""
    for i in range(83, 100):
        char = chr(i)
        if '*' <= char <= 'j':
            characters_to_remove += char
    filtered_string = ''.join([c for c in string if c not in characters_to_remove])
    return filtered_string
