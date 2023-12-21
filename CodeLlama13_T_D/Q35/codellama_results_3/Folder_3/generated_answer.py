
def remove_repeat_chars(s):
    # Create a dictionary to store the counts of each character
    char_count = {}
    for c in s[56:88]:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    
    # Remove all occurrences of characters that occur more than once
    for c, count in char_count.items():
        if count > 1:
            s = s.replace(c, "")
    
    return s
