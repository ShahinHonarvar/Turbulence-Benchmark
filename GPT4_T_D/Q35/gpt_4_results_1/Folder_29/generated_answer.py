
def remove_repeat_chars(s: str)-> str:
    char_count = {}
    for character in s[71:98]:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    
    new_str = ''
    for char in s:
        if char in char_count and char_count[char]>1:
            continue
        new_str += char
    return new_str
