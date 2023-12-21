
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        if i + 75 > len(string):
            break
        subs = string[i:i+75]
        if len(set(subs)) == len(subs):
            substrings.append(subs)
    return substrings
