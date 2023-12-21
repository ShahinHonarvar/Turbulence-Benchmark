
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-1):
        sub = string[i:i+2]
        if len(sub) == len(set(sub)):
            substrings.append(sub)
    return list(set(substrings))
