
def remove_repeat_chars(string):
    char_count = {}
    for i in range(2, 5):
        if string[i] in char_count:
            char_count[string[i]] += 1
        else:
            char_count[string[i]] = 1
    
    new_string = ''
    for c in string:
        if c not in char_count or char_count[c] <= 1:
            new_string += c
        elif c in char_count and char_count[c] > 1:
            char_count[c] -= 1
    
    return new_string
