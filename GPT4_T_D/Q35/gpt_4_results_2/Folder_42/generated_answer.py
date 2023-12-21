
def remove_repeat_chars(s):
    sub_str = s[19:60]
    to_remove = {c for c in sub_str if sub_str.count(c) > 1}
    
    result_chars = [c for c in s if c not in to_remove]
    
    return ''.join(result_chars)
