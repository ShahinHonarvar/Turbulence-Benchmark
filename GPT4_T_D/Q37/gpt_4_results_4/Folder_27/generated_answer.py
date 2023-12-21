
def filter_chars(s):
    chars_to_remove = set()
    for i in range(43, min(81, len(s))):
        if '=' <= s[i] <= 'E':
            chars_to_remove.add(s[i])
    result = ""
    for character in s:
        if character not in chars_to_remove:
            result += character
    return result
