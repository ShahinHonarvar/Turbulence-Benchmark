
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)-37):
            substring = string[i:j]
            if len(set(substring)) == 38 and all(c not in substrings for c in substring):
                substrings.append(substring)
    return substrings
