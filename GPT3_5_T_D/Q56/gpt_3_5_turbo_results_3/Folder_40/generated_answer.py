
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-1):
        substring = string[i:i+2]
        if len(substring) == 2 and substring[0] != substring[1]:
            substrings.append(substring)
    return list(set(substrings))
