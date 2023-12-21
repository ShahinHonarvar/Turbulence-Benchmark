
def filter_chars(s):
    indices = range(44, 49)
    filtered_chars = []
    for i in indices:
        if s[i].isalpha() and s[i] not in filtered_chars:
            filtered_chars.append(s[i])
    return ''.join([c if c in filtered_chars else '' for c in s])
