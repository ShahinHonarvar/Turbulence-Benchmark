
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 78):
        substring = string[i:i+79]
        if len(substring) == 79 and not any(substring[j] in substrings for j in range(79)):
            substrings.append(substring)
    return substrings
