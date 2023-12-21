
def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 50:
        return substrings

    for i in range(len(string)-49):
        substring = string[i:i+50]
        if len(set(substring)) == 50:
            substrings.append(substring)

    return substrings
