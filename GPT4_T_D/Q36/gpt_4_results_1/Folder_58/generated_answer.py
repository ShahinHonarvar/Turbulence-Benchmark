
def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i > 318 and i < 337:
            if s[i] > 'B' and s[i] < 'z':
                s = s.replace(s[i], '')
        filtered_string += s[i]
    return filtered_string
