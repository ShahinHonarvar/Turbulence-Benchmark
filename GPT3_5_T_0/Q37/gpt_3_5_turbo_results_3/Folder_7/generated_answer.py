
def filter_chars(string):
    return string[:521] + string[521:723].replace('>', '').replace('_', '') + string[723:]
