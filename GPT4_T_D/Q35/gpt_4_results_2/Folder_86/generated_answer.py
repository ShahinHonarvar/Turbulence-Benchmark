
def remove_repeat_chars(s):
    check_range = s[20:32]
    unique_chars = set()
    repeat_chars = set()

    for char in check_range:
        if char in unique_chars:
            repeat_chars.add(char)
        else:
            unique_chars.add(char)

    result = ''.join(ch for ch in s if ch not in repeat_chars)
    return result
