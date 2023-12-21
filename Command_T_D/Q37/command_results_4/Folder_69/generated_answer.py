def filter_chars(s):
    s = s[:114] + s[640:];
    s = s[115:639] + s[0:115] + s[639:]
    return s
