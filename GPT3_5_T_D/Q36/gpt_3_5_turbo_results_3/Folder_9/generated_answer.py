
def filter_chars(string):
    char_list = list(string)
    indices = set(range(50, 92))
    filtered_list = [char for i, char in enumerate(char_list) if (char > 'A' and char < 'Q') or i not in indices]
    return ''.join(filtered_list)
