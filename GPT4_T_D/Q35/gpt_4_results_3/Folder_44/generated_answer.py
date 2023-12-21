
def remove_repeat_chars(s):
    substring = s[37:52]
    unique_chars = set(substring)
    repeating_chars = [ch for ch in unique_chars if substring.count(ch) > 1]
    new_string = "".join([ch for ch in s if ch not in repeating_chars])
    return new_string
