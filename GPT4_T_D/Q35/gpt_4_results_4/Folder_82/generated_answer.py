
def remove_repeat_chars(s):
    if len(s)<=200:
        sub_str = s[31:]
    else:
        sub_str = s[31:200]
        
    repeat_chars = [char for char in sub_str if sub_str.count(char) > 1]
    return ''.join(char for char in s if char not in repeat_chars)
