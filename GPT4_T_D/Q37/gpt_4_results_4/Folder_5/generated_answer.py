
def filter_chars(s):
    chars_to_remove = set([c for c in s[24:83] if '5' <= c <= '<'])
    output = ""
    for c in s:
        if c not in chars_to_remove:
            output += c
    return output
