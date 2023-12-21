
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 80):
        sub = string[i:i+81]
        if len(set(sub)) == len(sub):
            substrings.append(sub)
    return substrings
