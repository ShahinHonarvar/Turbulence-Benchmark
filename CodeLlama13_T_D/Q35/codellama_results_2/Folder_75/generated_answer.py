
def remove_repeat_chars(s):
    seen = {}
    for i in range(20, 51):
        if s[i] in seen and seen[s[i]] == 1:
            del seen[s[i]]
        else:
            seen[s[i]] = 1
    return "".join([c for c in s if c not in seen])
