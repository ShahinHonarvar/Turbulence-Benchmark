
def filter_chars(s):
    characters_to_remove = [char for char in s[324:526] if char > ')' and char < 'O']
    for char in characters_to_remove:
        s = s.replace(char, '')
    return s
