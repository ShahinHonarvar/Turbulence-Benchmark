
def remove_repeat_chars(string):
    indices = set(range(476, 709))
    char_counts = {}
    for i, char in enumerate(string):
        if i in indices:
            char_counts[char] = char_counts.get(char, 0) + 1
    
    result = ''
    for char in string:
        if char not in char_counts or char_counts[char] == 1:
            result += char
    
    return result
