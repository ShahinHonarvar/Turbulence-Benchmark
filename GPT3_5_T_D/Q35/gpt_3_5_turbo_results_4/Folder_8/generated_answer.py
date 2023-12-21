
def remove_repeat_chars(string):
    char_counts = {}
    for i in range(len(string)):
        if 45 < i < 48 and string[i] in char_counts:
            char_counts[string[i]] += 1
        elif 45 < i < 48:
            char_counts[string[i]] = 1
    
    new_string = ''
    for i in range(len(string)):
        if 45 < i < 48 and string[i] in char_counts and char_counts[string[i]] > 1:
            char_counts[string[i]] -= 1
        elif not (45 < i < 48) or (45 < i < 48 and string[i] not in char_counts):
            new_string += string[i]
    
    return new_string
