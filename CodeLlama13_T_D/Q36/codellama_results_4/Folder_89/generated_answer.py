
def filter_chars(s):
    chars = []
    for i in range(len(s)):
        if 57 <= ord(s[i]) < 69 and s[i] != '(':
            chars.append(s[i])
    return "".join(chars)
