
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 32):
        substring = s[i:i+33]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return list(set(substrings))
