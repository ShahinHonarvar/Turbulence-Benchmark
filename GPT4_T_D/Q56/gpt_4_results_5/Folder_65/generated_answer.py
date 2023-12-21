
def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 80):
        substring = s[i:i+81]
        if len(set(substring)) == len(substring):
            result.add(substring)
    return list(result)
