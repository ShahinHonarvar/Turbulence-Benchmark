
def filter_chars(string):
    string_list = list(string)
    filtered_list = []
    for index, char in enumerate(string_list):
        if index < 44 or index >= 59:
            filtered_list.append(char)
        elif char > '/' and char < '6':
            filtered_list = [c for c in filtered_list if c != char]
    return ''.join(filtered_list)
