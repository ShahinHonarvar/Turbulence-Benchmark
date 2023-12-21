
def remove_repeat_chars(s):
    unique_chars = set(s[2:7])
    filtered_chars = [char for char in s if s[2:7].count(char) <= 1 or char not in unique_chars]
    return ''.join(filtered_chars)
