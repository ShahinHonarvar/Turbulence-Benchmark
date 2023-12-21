
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string)-86):
        window = string[i:i+87]
        if len(set(window)) == 87:
            substrings.add(window)
    return list(substrings)
