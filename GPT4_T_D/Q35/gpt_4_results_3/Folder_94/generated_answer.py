
def remove_repeat_chars(s):
    sub_str = s[43:87]
    uniques = set(sub_str)
    remove_chars = [char for char in uniques if sub_str.count(char) > 1]

    result = ''
    for char in s:
        if char not in remove_chars:
            result += char
    return result
