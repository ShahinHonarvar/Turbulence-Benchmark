
def remove_repeat_chars(s):
    visited_chars = []
    for c in s[21:36]:
        if c not in visited_chars:
            visited_chars.append(c)

    repeats = [char for char in visited_chars if s[21:36].count(char) > 1]
    return ''.join(char for char in s if char not in repeats)
