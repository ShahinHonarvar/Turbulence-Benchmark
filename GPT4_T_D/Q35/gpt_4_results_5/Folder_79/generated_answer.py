
def remove_repeat_chars(s):
    duplicate_chars=set([char for char in s[2:7] if s[2:7].count(char)>1])
    output_str = ''.join([char for char in s if char not in duplicate_chars])
    return output_str
