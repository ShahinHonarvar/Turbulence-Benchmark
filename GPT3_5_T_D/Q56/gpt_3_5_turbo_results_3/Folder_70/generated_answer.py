
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-11):
        substring = string[i:i+12]
        if len(set(substring)) == 12:
            substrings.append(substring)
    return list(set(substrings))
