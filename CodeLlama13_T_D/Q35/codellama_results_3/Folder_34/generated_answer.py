
def remove_repeat_chars(s):
    seen = {}
    new_str = ''
    for i, char in enumerate(s[70:200]):
        if char not in seen or seen[char] >= 2:
            continue
        else:
            seen[char] += 1
            new_str += char
    return new_str + s[:70] + s[200:]
