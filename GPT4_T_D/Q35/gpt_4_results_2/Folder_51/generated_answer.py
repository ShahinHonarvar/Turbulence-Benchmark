
def remove_repeat_chars(s):
    str_subsection = s[7:9]
    for char in str_subsection:
        if str_subsection.count(char) > 1:
            s = s.replace(char, '')
    return s
