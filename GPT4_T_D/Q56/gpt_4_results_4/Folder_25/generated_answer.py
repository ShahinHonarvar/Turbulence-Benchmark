
def all_substring_of_size_n(str):
    substrings = set()
    for i in range(len(str) - 66):
        substring = str[i:i+67]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)
