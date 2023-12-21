
def filter_chars(s):
    filtered_chars = []
    for i in range(28, 75):
        if 'A' < s[i] < 'i':
            filtered_chars.append(s[i])
    for char in filtered_chars:
        s = s.replace(char, '')
    return s
