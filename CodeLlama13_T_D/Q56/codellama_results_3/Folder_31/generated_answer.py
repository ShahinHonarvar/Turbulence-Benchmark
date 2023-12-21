
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 45):
        substring = string[i:i+46]
        if len(set(substring)) == 46 and not any(substring in s for s in substrings):
            substrings.append(substring)
    return substrings
