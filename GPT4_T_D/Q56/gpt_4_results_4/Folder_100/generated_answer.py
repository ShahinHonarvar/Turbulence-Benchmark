
def all_substring_of_size_n(s):
    n = 92
    result = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if len(set(substring)) == len(substring):
            if substring not in result:
                result.append(substring)
    return result
