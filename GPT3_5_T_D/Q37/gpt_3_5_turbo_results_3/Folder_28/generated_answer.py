
def filter_chars(string):
    string_chars = list(string)
    filtered_chars = []
    for idx, char in enumerate(string_chars):
        if 20 <= idx <= 79 and '!' <= char <= 'T':
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)
