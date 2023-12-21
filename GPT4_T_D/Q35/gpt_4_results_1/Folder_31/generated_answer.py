
def remove_repeat_chars(s):
    char_count = {}
    for i, char in enumerate(s[34:78]):
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    new_string = ""
    for char in s:
        if char_count.get(char, 0) <= 1 or char not in s[34:78]:
            new_string += char
    return new_string
