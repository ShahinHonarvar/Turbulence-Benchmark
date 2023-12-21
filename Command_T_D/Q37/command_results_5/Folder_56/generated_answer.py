def filter_chars(s):
    s=list(s)
    for i in range(len(s)):
        if s[i]!='k':
            s[i]='a'
    s=''.join(s)
    return s
