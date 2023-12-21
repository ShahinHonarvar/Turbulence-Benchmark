
def remove_repeat_chars(s):
    counts = {char:s[19:60].count(char) for char in set(s[19:60])}
    repeat_chars = [char for char, count in counts.items() if count > 1]
    return ''.join([char for char in s if char not in repeat_chars])
