
def remove_repeat_chars(s):
    segment = s[37:54]
    unique_chars = set()
    repeating_chars = set()

    for char in segment:
        if char in unique_chars:
            repeating_chars.add(char)
        else:
            unique_chars.add(char)

    return ''.join(char for char in s if char not in repeating_chars)
