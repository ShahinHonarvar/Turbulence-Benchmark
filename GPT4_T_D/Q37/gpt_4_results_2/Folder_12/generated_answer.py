
def filter_chars(str_arg):
    filtered_substring = [ch for i, ch in enumerate(str_arg[19:91]) if not('F' <= ch <= 'h')]
    new_string = str_arg[:19] + ''.join(filtered_substring) + str_arg[91:]
    return new_string
