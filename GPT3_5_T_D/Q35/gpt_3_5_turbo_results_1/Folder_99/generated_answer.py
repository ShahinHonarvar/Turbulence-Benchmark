
def remove_repeat_chars(s):
    return s[:450] + ''.join([c for c in s[450:905] if s[450:905].count(c) == 1]) + s[905:]
