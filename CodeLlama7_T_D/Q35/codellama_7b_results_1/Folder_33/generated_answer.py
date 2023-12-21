 def remove_repeat_chars(s):
    for c in set(s):
        i = s.find(c) + 1
        while i < len(s) and s[i] == c:
            s = s[:i] + s[i+1:]
    return s
