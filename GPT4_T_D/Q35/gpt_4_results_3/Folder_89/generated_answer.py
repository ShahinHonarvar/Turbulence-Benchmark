
def remove_repeat_chars(input_string):
    sub_string = input_string[56:84]
    char_counts = {}
    for char in sub_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for char, count in char_counts.items():
        if count > 1:
            input_string = input_string.replace(char, '')
    return input_string
