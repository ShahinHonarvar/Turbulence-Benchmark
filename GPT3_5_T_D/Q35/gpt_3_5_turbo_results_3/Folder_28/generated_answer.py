
def remove_repeat_chars(string):
    char_counts = {}
    for i in range(len(string)):
        if 86 < i < 99:
            char = string[i]
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    
    altered_string = ''
    for char in string:
        if char not in char_counts or (char_counts[char] == 1 and (86 < string.index(char) < 99)):
            altered_string += char
    
    return altered_string
