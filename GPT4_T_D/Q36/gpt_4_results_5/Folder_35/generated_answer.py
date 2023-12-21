
def filter_chars(phrase):
    filter_chars = [char for char in phrase[164:658] if char > '(' and char < ']']
    for char in filter_chars:
        phrase = phrase.replace(char,'')
    return phrase
