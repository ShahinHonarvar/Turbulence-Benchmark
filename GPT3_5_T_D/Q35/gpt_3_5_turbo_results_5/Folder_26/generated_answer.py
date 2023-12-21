
def remove_repeat_chars(string):
    char_counts = {}
    for i in range(68, 99):
        char = string[i]
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    result = ""
    for char in string:
        if char not in char_counts or char_counts[char] <= 1:
            result += char
    
    return result
