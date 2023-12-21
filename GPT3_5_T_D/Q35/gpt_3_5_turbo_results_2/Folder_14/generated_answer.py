
def remove_repeat_chars(string):
    char_count = {}
    for i in range(2, 5):
        char = string[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    altered_string = ''
    for char in string:
        if char not in char_count or char_count[char] <= 1:
            altered_string += char

    return altered_string
