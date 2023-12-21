
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-67):
        substring = string[i:i+68]
        if len(set(substring)) == 68:
            substrings.append(substring)
    return list(set(substrings))
