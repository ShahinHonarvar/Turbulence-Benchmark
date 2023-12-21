
def remove_repeat_chars(s):
    char_counts = {char: s[11:77].count(char) for char in s[11:77]}
    for char, count in char_counts.items():
        if count > 1:
            s = s.replace(char, "")
    return s
