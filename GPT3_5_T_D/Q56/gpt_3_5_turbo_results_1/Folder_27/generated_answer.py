
def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 57:
        return substrings

    start = 0
    end = 57
    while end <= len(string):
        substring = string[start:end]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
        start += 1
        end += 1

    return list(set(substrings))
