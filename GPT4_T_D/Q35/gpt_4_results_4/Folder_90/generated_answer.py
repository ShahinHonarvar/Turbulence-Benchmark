
def remove_repeat_chars(s):
    repeated_chars = set()
    for i in range(307, 807):
        if s[i] in s[307:i] or s[i] in s[i+1:808]:
            repeated_chars.add(s[i])
    return ''.join([c for c in s if c not in repeated_chars])
