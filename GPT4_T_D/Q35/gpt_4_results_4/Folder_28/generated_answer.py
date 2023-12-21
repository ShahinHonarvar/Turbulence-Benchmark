
def remove_repeat_chars(s):
    char_dict= {}
    for i in range(87, 99):
        if i < len(s):
            if s[i] in char_dict:
                char_dict[s[i]] += 1
            else:
                char_dict[s[i]] = 1
    unique_chars = [key for key, value in char_dict.items() if value==1]
    result = [char for char in s if char in unique_chars or (s.index(char) <=86 or s.index(char)>=99 )]
    return ''.join(result)
