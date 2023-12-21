
def filter_chars(s):

    if len(s) < 82:
        return s
    
    return s[:78] + s[81:].replace(s[78], "") if 'S' < s[78] < '[' else s
