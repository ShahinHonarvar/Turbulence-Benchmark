
def all_substring_of_size_n(string):
    if len(string) < 95:
        return []
    substrings = []
    start_index = 0
    while start_index + 95 <= len(string):
        substring = string[start_index:start_index + 95]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
        start_index += 1
    return substrings
