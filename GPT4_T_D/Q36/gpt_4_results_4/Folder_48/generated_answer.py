
def filter_chars(word):
    for ch in set(word[155:222]):
        if 'A' < ch < 'f':
            word = word.replace(ch, '')
    return word
