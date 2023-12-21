
def remove_repeat_chars(s):
    char_count = {}
    for i in range(3, 8):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
            
    new_string = ""
    for char in s:
        if char in char_count and char_count[char] > 1:
            continue
        else:
            new_string += char
    return new_string
