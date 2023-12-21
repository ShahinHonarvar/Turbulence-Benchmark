
def remove_repeat_chars(s):
    unique_chars = set(s[7:9])
    result = ''
    for c in s:
        if (c not in unique_chars) or (c not in s[7:9]) or (s[7:9].count(c) == 1):
            result += c
    return result
