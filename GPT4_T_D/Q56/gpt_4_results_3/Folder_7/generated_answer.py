
def all_substring_of_size_n(string):
    n = 117
    substrings = [string[i:i+n] for i in range(len(string)-n+1)]
    unique_substrings = list(set(substrings))
    result = [s for s in unique_substrings if len(set(s)) == len(s)]
    return result
