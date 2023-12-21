
def remove_repeat_chars(string):
    char_count = {}
    for i in range(72, 93):
        char = string[i]
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    altered_string = ""
    for i in range(len(string)):
        if string[i] not in char_count or char_count[string[i]] == 0:
            altered_string += string[i]
        else:
            char_count[string[i]] -= 1
    
    return altered_string
