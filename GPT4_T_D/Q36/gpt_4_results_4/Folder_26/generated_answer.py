
def filter_chars(string):
    string_to_filter = string[44:83]
    filtered_chars = [char for char in string_to_filter if not(':' < char < 'Q')]
    for char in filtered_chars:
        string = string.replace(char, '')
    return string
