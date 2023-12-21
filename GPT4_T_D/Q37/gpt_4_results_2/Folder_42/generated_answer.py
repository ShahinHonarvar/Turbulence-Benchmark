
def filter_chars(s):
    chars_to_remove=[]
    for i in range(73, 75):
        if i < len(s) and s[i] >= 'U' and s[i] <= 'l':
            chars_to_remove.append(s[i])
    modified_s = ''.join([c for c in s if c not in chars_to_remove])
    return modified_s
