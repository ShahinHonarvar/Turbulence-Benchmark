
def all_substring_of_size_n(string):
    n = 61
    results = []
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if len(substring) == len(set(substring)):
            results.append(substring)
    return list(set(results))
