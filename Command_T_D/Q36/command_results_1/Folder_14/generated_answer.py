def filter_chars(s):
    for c in range(ord('Z')+1,ord('c')+1):
        s=s.replace(chr(c),'')
    return s
