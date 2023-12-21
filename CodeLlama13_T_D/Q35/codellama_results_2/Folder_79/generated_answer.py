
def remove_repeat_chars(s):
    seen = {}
    new_str = ''
    for i, char in enumerate(s[1:-7]):
        if char not in seen:
            seen[char] = 0
        else:
            seen[char] += 1
        if seen[char] < 2:
            new_str += char
    return new_str
