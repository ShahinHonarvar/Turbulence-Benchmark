def remove_repeat_chars(s):
    new = ''
    for i in range(len(s)):
        if i < 37:
            new += s[i]
        elif i > 43:
            break
        elif s[i] in s[37:43]:
            new += s[i]
    return new
