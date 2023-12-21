
def remove_repeat_chars(s):
    char_counts = {char: s[331:543].count(char) for char in set(s[331:543])}
    repeated_chars = [char for char, count in char_counts.items() if count > 1]
    return ''.join([char for i, char in enumerate(s) if char not in repeated_chars or i <= 330 or i >= 543])
