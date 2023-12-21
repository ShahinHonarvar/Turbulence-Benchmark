
def remove_repeat_chars(s):
    mid_string = s[57:90]
    final_string = s[:57] + s[90:]
    unique_chars = set(mid_string)
    for char in unique_chars:
        if mid_string.count(char) > 1:
            final_string = final_string.replace(char, '')
    return final_string
