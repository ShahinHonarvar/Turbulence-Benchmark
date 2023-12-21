
def remove_repeat_chars(s):
    char_counts = {}
    for char in s[451:905]:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    result = []
    for char in s:
        if char_counts.get(char, 0) <= 1 or char not in s[451:905]:
            result.append(char)
    return ''.join(result)
