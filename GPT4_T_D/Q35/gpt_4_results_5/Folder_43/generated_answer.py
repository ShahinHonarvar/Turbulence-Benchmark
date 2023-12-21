
def remove_repeat_chars(string):
    substring = string[11:28]
    result = ''
    for ch in substring:
        if substring.count(ch) > 1:
            string = string.replace(ch, '')
        else:
            result += ch
    return string[:11] + result + string[28:]
