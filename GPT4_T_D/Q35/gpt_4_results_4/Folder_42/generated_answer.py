
def remove_repeat_chars(s):
    duplicates = set([i for i in s[19:60] if s[19:60].count(i) > 1])
    result = ''.join([i for i in s if i not in duplicates])
    return result
