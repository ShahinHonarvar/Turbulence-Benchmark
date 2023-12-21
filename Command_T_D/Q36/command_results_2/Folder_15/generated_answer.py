def filter_chars(s):
    lst = [char for char in s[2:-2]]
    for char in lst:
        if char > 'h' and char < 'k':
            lst.remove(char)
    return ''.join(lst)
