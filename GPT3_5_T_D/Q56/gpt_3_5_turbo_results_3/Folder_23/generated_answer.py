
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i+42, len(string)+1):
            substring = string[i:j]
            if len(substring) == 42 and len(set(substring)) == 42:
                substrings.append(substring)
    return list(set(substrings))
