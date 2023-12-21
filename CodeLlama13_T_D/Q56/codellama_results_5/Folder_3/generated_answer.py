
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            if len(substring) == 93 and not any(substring[k] in substring[:k] for k in range(1, len(substring))):
                substrings.append(substring)
    return substrings
