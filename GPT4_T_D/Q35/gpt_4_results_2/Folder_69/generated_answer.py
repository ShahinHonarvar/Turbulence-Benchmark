
def remove_repeat_chars(s):
    char_count = {}
    modified_string = ""
    for i, char in enumerate(s):
        if 39 < i < 43:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        if char not in char_count or char_count[char] == 1:
            modified_string += char
    return modified_string
