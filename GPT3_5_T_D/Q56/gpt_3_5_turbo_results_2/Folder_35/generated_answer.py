
def all_substring_of_size_n(string):
    result = []
    for i in range(len(string)-26):
        substring = string[i:i+27]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result
