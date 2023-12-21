
def filter_chars(s):
    to_remove = []
    for i in range(71, 74):
        if i < len(s) and 'A' < s[i] < 'U':
            to_remove.append(s[i])
    
    new_s = ''
    for char in s:
        if char not in to_remove:
            new_s += char
            
    return new_s
