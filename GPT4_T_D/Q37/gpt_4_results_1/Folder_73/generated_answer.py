
def filter_chars(s):
    altered_string = s
    for i in range(22, min(86, len(s))):
        if '7' <= s[i] <= 'e':
            altered_string = altered_string.replace(s[i], "")
    return altered_string
