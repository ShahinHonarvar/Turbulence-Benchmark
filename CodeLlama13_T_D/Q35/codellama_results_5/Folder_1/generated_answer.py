
def remove_repeat_chars(s):
    seen = {}
    for i in range(17, 89):
        if s[i] in seen:
            del seen[s[i]]
        else:
            seen[s[i]] = True
    return ''.join(seen)
