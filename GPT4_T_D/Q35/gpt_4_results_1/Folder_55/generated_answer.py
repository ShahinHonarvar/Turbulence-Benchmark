
def remove_repeat_chars(s):
    rare_chars = set(s[11:100])
    repeat_chars = set([c for c in rare_chars if s[11:100].count(c) > 1])
    result_str = ""
    
    for ch in s:
        if ch not in repeat_chars:
            result_str+=ch

    return result_str
