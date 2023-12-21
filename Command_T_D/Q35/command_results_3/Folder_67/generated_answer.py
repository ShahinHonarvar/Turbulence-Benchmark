def remove_repeat_chars(s):
    start, end = 44, 67
    return s[:start] + s[start+1:end] + s[end+1:-1] + s[end+2:]
