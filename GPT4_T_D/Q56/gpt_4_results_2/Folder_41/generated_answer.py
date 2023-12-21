
def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 73):
        substring = s[i:i+74]
        if len(set(substring)) == len(substring):
            result.add(substring)
    return list(result)
