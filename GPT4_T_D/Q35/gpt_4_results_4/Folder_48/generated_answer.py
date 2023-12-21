
def remove_repeat_chars(string):
    char_counts = dict()
    for i in range(410, 502):
        if string[i] in char_counts:
            char_counts[string[i]] += 1
        else:
            char_counts[string[i]] = 1
            
    for char, count in char_counts.items():
        if count > 1:
            string = string.replace(char, '')
    return string
