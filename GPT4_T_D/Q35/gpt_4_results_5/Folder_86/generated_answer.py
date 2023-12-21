
def remove_repeat_chars(s):
    start, end = 19, 32
    repeats = set([char for char in s[start+1:end] if s[start+1:end].count(char) > 1])
    return ''.join([char for i, char in enumerate(s) if s.count(char) == 1 or char not in repeats])
