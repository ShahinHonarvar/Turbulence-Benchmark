
def remove_repeat_chars(string):
    char_count = {}
    for i in range(20, 93):
        if string[i] in char_count:
            char_count[string[i]] += 1
        else:
            char_count[string[i]] = 1

    new_string = ""
    for i in range(len(string)):
        if char_count[string[i]] == 0 or string[i] not in char_count:
            new_string += string[i]
        else:
            char_count[string[i]] -= 1
    
    return new_string
