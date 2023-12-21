
def remove_repeat_chars(s):
    seen = {}
    for i in range(13, 70):
        if s[i] in seen and seen[s[i]] > 0:
            seen[s[i]] -= 1
            s = s[:i-seen[s[i]]] + s[i+1:]
    return s
