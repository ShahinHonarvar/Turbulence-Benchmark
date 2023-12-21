
def remove_repeat_chars(s):
    repeated_chars = {char for char, count in dict.fromkeys(s[11:76]).items() if s.count(char) > 1}
    return ''.join(char for char in s if char not in repeated_chars)
