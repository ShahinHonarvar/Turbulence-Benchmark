
def all_substring_of_size_n(string):
    distinct_substrings = []
    for i in range(len(string)-22+1):
        substring = string[i:i+22]
        if len(set(substring)) == len(substring):
            distinct_substrings.append(substring)
    return distinct_substrings
