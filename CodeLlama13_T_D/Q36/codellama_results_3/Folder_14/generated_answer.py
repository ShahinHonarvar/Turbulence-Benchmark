
def filter_chars(string):
    new_str = ''
    for i in range(len(string)):
        if string[i].isalpha() and string[i].lower() not in 'zyxwvutsrqponmlkjihgfedcba':
            new_str += string[i]
    return new_str
