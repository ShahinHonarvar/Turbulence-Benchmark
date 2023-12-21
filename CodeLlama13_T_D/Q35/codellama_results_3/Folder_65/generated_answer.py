
def remove_repeat_chars(string):
    # Create a dictionary to store the counts of each character in the string
    char_counts = {}
    for char in string:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    
    # Remove all occurrences of characters that occur more than once between indices 51 and 76, both exclusive
    for char in list(char_counts):
        if char_counts[char] > 1 and 50 < string.index(char) < 77:
            string = string.replace(char, "")
    
    return string
