
def all_substring_of_size_n(s):
    list_of_substrings = []
    for i in range(len(s)-54):
        substring = s[i:i+55]
        if len(set(substring)) == len(substring):
            if substring not in list_of_substrings:
                list_of_substrings.append(substring)
    return list_of_substrings
