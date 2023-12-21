
def remove_repeat_chars(s):
    subsection = s[101:200]
    removed_chars = [char for char in set(subsection) if subsection.count(char) > 1]
    return ''.join(char for char in s if char not in removed_chars)
