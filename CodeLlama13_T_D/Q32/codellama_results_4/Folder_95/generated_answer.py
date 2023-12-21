
def insert_after_character(s):
    return ''.join('q' + s[i:] if s[i] == 'j' else s[i] for i in range(len(s)))
