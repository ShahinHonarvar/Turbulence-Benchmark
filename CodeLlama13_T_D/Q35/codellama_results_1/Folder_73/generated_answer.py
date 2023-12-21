
def remove_repeat_chars(string):
    char_count = {}
    for i in range(10, 76):
        if string[i] in char_count:
            char_count[string[i]] += 1
        else:
            char_count[string[i]] = 1
    
    new_str = ""
    for i in range(len(string)):
        if string[i] not in char_count or char_count[string[i]] == 0:
            new_str += string[i]
        else:
            char_count[string[i]] -= 1
    
    return new_str
