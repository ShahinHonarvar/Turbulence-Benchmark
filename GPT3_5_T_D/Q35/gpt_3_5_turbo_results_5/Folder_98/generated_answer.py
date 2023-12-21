
def remove_repeat_chars(string):
    char_count = {}
    for i, char in enumerate(string):
        if i < 7:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    new_string = ''
    for char in string:
        if char not in char_count or (0 < string.index(char) < 7 and char_count[char] == 1):
            new_string += char

    return new_string
