
def filter_chars(s):
    altered_s = list(s)
    for char in s[32:70]:
        if 'B' < char < 'v':
            while char in altered_s:
                altered_s.remove(char)
    return "".join(altered_s)
