
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-22):
        sub = string[i:i+23]
        if len(sub) == len(set(sub)):
            substrings.append(sub)
    return substrings
