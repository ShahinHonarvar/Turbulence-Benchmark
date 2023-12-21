
def remove_repeat_chars(s):
    # Create a dictionary to keep track of the characters and their counts
    char_counts = {}
    for i in range(27, 96):
        char = s[i]
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    
    # Remove all characters that have a count greater than 1
    for char, count in char_counts.items():
        if count > 1:
            s = s.replace(char, "")
    
    return s
