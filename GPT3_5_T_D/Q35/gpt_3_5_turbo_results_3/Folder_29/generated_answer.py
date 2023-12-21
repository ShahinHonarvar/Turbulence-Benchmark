
def remove_repeat_chars(string):
    char_counts = {}
    for i in range(len(string)):
        if 70 < i < 98:
            if string[i] in char_counts:
                char_counts[string[i]] += 1
            else:
                char_counts[string[i]] = 1
    
    new_string = ""
    for char in string:
        if char not in char_counts or (70 <= string.index(char) < 98 and char_counts[char] < 2):
            new_string += char
    
    return new_string
