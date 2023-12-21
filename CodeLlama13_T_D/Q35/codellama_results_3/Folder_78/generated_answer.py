
def remove_repeat_chars(s):
    seen = {}
    for i in range(62, 96):
        if s[i] in seen:
            continue
        else:
            seen[s[i]] = True
    return "".join([c for c in s if c not in seen])
