 def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if s[i] != 'H' and s[i] != '|':
            result += s[i]
    return result
