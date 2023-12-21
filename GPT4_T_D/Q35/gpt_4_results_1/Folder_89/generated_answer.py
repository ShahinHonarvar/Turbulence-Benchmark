
def remove_repeat_chars(s):
    checked_chars = set()
    repeated_chars = set()
    for i in range(56, min(84, len(s))):
        if s[i] in checked_chars:
            repeated_chars.add(s[i])
        else:
            checked_chars.add(s[i])
    return ''.join([char for char in s if char not in repeated_chars])
