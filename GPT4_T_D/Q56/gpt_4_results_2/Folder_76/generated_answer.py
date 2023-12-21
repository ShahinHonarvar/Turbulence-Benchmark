
def all_substring_of_size_n(s):
    result_set = set()
    for i in range(len(s)-148):
        substring = s[i:i+149]
        if len(set(substring)) == len(substring):
            result_set.add(substring)
    return list(result_set)
