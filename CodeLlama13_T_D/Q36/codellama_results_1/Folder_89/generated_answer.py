
def filter_chars(s):
    result = ""
    for i in range(len(s)):
        if s[i] == '(' or s[i] == ')':
            continue
        else:
            result += s[i]
    return result
