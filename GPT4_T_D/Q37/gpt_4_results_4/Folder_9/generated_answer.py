
def filter_chars(s):
    filtered_chars = []
    for i in range(38, min(100, len(s))):
        if 'A' <= s[i] <= 'Q':
            filtered_chars.append(s[i])
    return ''.join([char for char in s if char not in filtered_chars])
