
def filter_chars(mystr):
    relevant_chars = set([c for c in mystr[73:93] if c > '<' and c < 'J'])
    new_str = ''.join([c for c in mystr if c not in relevant_chars])
    return new_str
