
def filter_chars(s):
    start = 13
    end = 28
    c = 'c'
    n = 'n'
    filtered_string = ''

    for char in s:
        if start <= s.index(char) <= end and ord(char) >= ord(c) and ord(char) <= ord(n):
            continue

        else:

            filtered_string += char

    return filtered_string
