
def remove_repeat_chars(string):
    seen = {}
    new_str = ""
    for char in string[:10]:
        if char not in seen:
            new_str += char
            seen[char] = True
    return new_str + string[10:]
