
def remove_repeat_chars(s):
    observed_chars = set()
    repeat_chars = set()

    for index, char in enumerate(s[17:87], 17):
        if char in observed_chars:
            repeat_chars.add(char)
        observed_chars.add(char)
    
    return ''.join(char for index, char in enumerate(s) if char not in repeat_chars)
