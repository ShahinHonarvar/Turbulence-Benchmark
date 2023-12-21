
def remove_repeat_chars(string):
    char_count = {}
    for i in range(46, 91):
        if string[i] in char_count:
            char_count[string[i]] += 1
        else:
            char_count[string[i]] = 1
    
    result = ""
    for i in range(len(string)):
        if char_count[string[i]] == 1 or i < 46 or i > 90:
            result += string[i]
    
    return result
