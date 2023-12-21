
def remove_repeat_chars(string):
    # create a dictionary to keep track of the characters and their counts
    char_counts = {}
    for i in range(44, 78):
        if string[i] not in char_counts:
            char_counts[string[i]] = 1
        else:
            char_counts[string[i]] += 1
    
    # remove all occurrences of the characters that occur more than once
    for i in range(44, 78):
        if string[i] in char_counts and char_counts[string[i]] > 1:
            string = string.replace(string[i], '')
    
    return string
