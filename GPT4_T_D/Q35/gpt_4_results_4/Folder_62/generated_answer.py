
def remove_repeat_chars(s):
    s = list(s)
    alter = []
    for i in range(51, 92):
        if s[i] in s[i+1:93]:
            alter.append(s[i])
    for char in alter:
        while char in s:
            s.remove(char)
    return ''.join(s)
