
def remove_repeat_chars(s):
    repeat_chars = set([i for i in s[477:709] if s[477:709].count(i) > 1])
    result = "".join([i for i in s if i not in repeat_chars])
    return result
