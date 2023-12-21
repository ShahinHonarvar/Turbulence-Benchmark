
def remove_repeat_chars(string):
    indices = set(range(20, 200))
    char_count = {}
    for i, char in enumerate(string):
        if i in indices:
            char_count[char] = char_count.get(char, 0) + 1
    
    new_string = ""
    for char in string:
        if char not in char_count or char_count[char] <= 1:
            new_string += char
    
    return new_string
