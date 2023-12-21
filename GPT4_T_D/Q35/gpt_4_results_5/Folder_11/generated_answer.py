
def remove_repeat_chars(s):
    substring = s[49:76]
    to_remove = set([x for x in substring if substring.count(x) > 1])
    result = [x for x in s if x not in to_remove]
    return ''.join(result)
