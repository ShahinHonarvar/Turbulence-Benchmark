
def filter_chars(str):
    for i in range(54, min(63, len(str))):
        if str[i] >= ')' and str[i] <= '9':
            str = str.replace(str[i], '')
    return str
